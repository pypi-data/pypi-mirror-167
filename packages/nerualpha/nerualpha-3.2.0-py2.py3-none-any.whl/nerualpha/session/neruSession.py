from dataclasses import dataclass, field
from typing import Dict, List, Generic, TypeVar
from abc import ABC, abstractmethod

from nerualpha.IBridge import IBridge
from nerualpha.providers.events.eventEmitter import EventEmitter
from nerualpha.providers.events.IEventEmitter import IEventEmitter
from nerualpha.providers.logger.ILogContext import ILogContext
from nerualpha.providers.logger.ILogger import ILogger
from nerualpha.providers.logger.logContext import LogContext
from nerualpha.providers.logger.logger import Logger
from nerualpha.providers.logger.logLevels import LogLevels
from nerualpha.request.RequestHeaders import RequestHeaders
from nerualpha.services.commandService.ICommandService import ICommandService
from nerualpha.services.config.IConfig import IConfig
from nerualpha.services.jwt.IJwt import IJWT
from nerualpha.session.command import Command
from nerualpha.session.CommandHeaders import CommandHeaders
from nerualpha.session.IActionPayload import IActionPayload
from nerualpha.session.ICommand import ICommand
from nerualpha.session.IFilter import IFilter
from nerualpha.session.ISession import ISession
from nerualpha.session.wrappedCallback import WrappedCallback

@dataclass
class NeruSession(ISession):
    eventEmitter: IEventEmitter
    commandService: ICommandService
    logger: ILogger
    bridge: IBridge
    jwt: IJWT
    config: IConfig
    id: str
    def __init__(self,commandService,bridge,config,jwt,id):
        self.commandService = commandService
        self.id = id
        self.bridge = bridge
        self.config = config
        self.jwt = jwt
        self.eventEmitter = EventEmitter(self)
        self.logger = Logger(self)
    
    async def emitSessionCreatedEvent(self,ttl):
        await self.eventEmitter.emitSessionCreatedEvent(ttl)
    
    def createUUID(self):
        return self.bridge.uuid()
    
    def getToken(self):
        if self.config.debug:
            return None
        
        return self.jwt.getToken()
    
    def log(self,level,message,context = None):
        self.bridge.runBackgroundTask(self.logger.log(level,message,context))
    
    def wrapCallback(self,route,filters):
        wrappedCallback = WrappedCallback()
        wrappedCallback.filters = filters
        wrappedCallback.id = self.createUUID()
        wrappedCallback.instanceServiceName = self.config.instanceServiceName
        wrappedCallback.sessionId = self.id
        wrappedCallback.instanceId = self.config.instanceId
        wrappedCallback.path = route
        return wrappedCallback
    
    def constructCommandHeaders(self):
        commandHeaders = CommandHeaders()
        commandHeaders.traceId = self.createUUID()
        commandHeaders.instanceId = self.config.instanceId
        commandHeaders.sessionId = self.id
        commandHeaders.apiAccountId = self.config.apiAccountId
        commandHeaders.apiApplicationId = self.config.apiApplicationId
        commandHeaders.applicationName = self.config.instanceServiceName
        commandHeaders.applicationId = self.config.applicationId
        return commandHeaders
    
    def constructRequestHeaders(self):
        requestHeaders = RequestHeaders()
        requestHeaders.X_hyphen_Neru_hyphen_SessionId = self.id
        requestHeaders.X_hyphen_Neru_hyphen_ApiAccountId = self.config.apiAccountId
        requestHeaders.X_hyphen_Neru_hyphen_ApiApplicationId = self.config.apiApplicationId
        requestHeaders.X_hyphen_Neru_hyphen_InstanceId = self.config.instanceId
        requestHeaders.X_hyphen_Neru_hyphen_TraceId = self.bridge.uuid()
        token = self.getToken()
        if token is not None:
            requestHeaders.Authorization = f'Bearer {token}'
        
        return requestHeaders
    
    async def executeAction(self,actionPayload):
        try:
            commandHeaders = self.constructCommandHeaders()
            requestHeaders = self.constructRequestHeaders()
            payload = Command(commandHeaders,actionPayload)
            url = self.config.getExecutionUrl(actionPayload.provider)
            result = await self.commandService.executeCommand(url,payload,requestHeaders)
            context = LogContext(actionPayload.action,self.bridge.jsonStringify(actionPayload.payload),self.bridge.jsonStringify(result))
            self.log(LogLevels.info,f'Executing action: {actionPayload.action}, provider: {actionPayload.provider}',context)
            return result
        
        except Exception as e:
            context = LogContext(actionPayload.action,self.bridge.jsonStringify(actionPayload.payload),e.message)
            self.log(LogLevels.error,f'Error while executing action: {actionPayload.action}, provider: {actionPayload.provider}',context)
            raise e
        
    
    def reprJSON(self):
        dict = {}
        keywordsMap = {"from_":"from","del_":"del","import_":"import","type_":"type"}
        for key in self.__dict__:
            val = self.__dict__[key]

            if type(val) is list:
                parsedList = []
                for i in val:
                    if hasattr(i,'reprJSON'):
                        parsedList.append(i.reprJSON())
                    else:
                        parsedList.append(i)
                val = parsedList

            if hasattr(val,'reprJSON'):
                val = val.reprJSON()
            if key in keywordsMap:
                key = keywordsMap[key]
            dict.__setitem__(key.replace('_hyphen_', '-'), val)
        return dict
