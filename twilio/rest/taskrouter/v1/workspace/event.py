# coding=utf-8
"""
This code was generated by
\ / _    _  _|   _  _
 | (_)\/(_)(_|\/| |(/_  v1.0.0
      /       /       
"""

from twilio import values
from twilio.rest import deserialize
from twilio.rest.base import InstanceContext
from twilio.rest.base import InstanceResource
from twilio.rest.base import ListResource


class EventList(ListResource):

    def __init__(self, version, workspace_sid):
        """
        Initialize the EventList
        
        :param Version version: Version that contains the resource
        :param workspace_sid: Contextual workspace_sid
        
        :returns: EventList
        :rtype: EventList
        """
        super(EventList, self).__init__(version)
        
        # Path Solution
        self._kwargs = {
            'workspace_sid': workspace_sid,
        }
        self._uri = '/Workspaces/{workspace_sid}/Events'.format(**self._kwargs)

    def read(self, end_date=values.unset, event_type=values.unset,
             minutes=values.unset, reservation_sid=values.unset,
             start_date=values.unset, task_queue_sid=values.unset,
             task_sid=values.unset, worker_sid=values.unset,
             workflow_sid=values.unset, limit=None, page_size=None, **kwargs):
        limits = self._version.read_limits(limit, page_size)
        
        params = values.of({
            'EndDate': end_date,
            'EventType': event_type,
            'Minutes': minutes,
            'ReservationSid': reservation_sid,
            'StartDate': start_date,
            'TaskQueueSid': task_queue_sid,
            'TaskSid': task_sid,
            'WorkerSid': worker_sid,
            'WorkflowSid': workflow_sid,
            'PageSize': limits['page_size'],
        })
        params.update(kwargs)
        
        return self._version.read(
            self,
            EventInstance,
            self._kwargs,
            'GET',
            self._uri,
            limits['limit'],
            limits['page_limit'],
            params=params,
        )

    def page(self, end_date=values.unset, event_type=values.unset,
             minutes=values.unset, reservation_sid=values.unset,
             start_date=values.unset, task_queue_sid=values.unset,
             task_sid=values.unset, worker_sid=values.unset,
             workflow_sid=values.unset, page_token=None, page_number=None,
             page_size=None, **kwargs):
        params = values.of({
            'EndDate': end_date,
            'EventType': event_type,
            'Minutes': minutes,
            'ReservationSid': reservation_sid,
            'StartDate': start_date,
            'TaskQueueSid': task_queue_sid,
            'TaskSid': task_sid,
            'WorkerSid': worker_sid,
            'WorkflowSid': workflow_sid,
            'PageToken': page_token,
            'Page': page_number,
            'PageSize': page_size,
        })
        params.update(kwargs)
        
        return self._version.page(
            self,
            EventInstance,
            self._kwargs,
            'GET',
            self._uri,
            params=params,
        )

    def __call__(self, sid):
        """
        Constructs a EventContext
        
        :param sid: Contextual sid
        
        :returns: EventContext
        :rtype: EventContext
        """
        return EventContext(self._version, sid=sid, **self._kwargs)

    def __repr__(self):
        """
        Provide a friendly representation
        
        :returns: Machine friendly representation
        :rtype: str
        """
        return '<Twilio.Taskrouter.V1.EventList>'


class EventContext(InstanceContext):

    def __init__(self, version, workspace_sid, sid):
        super(EventContext, self).__init__(version)
        
        # Path Solution
        self._kwargs = {
            'workspace_sid': workspace_sid,
            'sid': sid,
        }
        self._uri = '/Workspaces/{workspace_sid}/Events/{sid}'.format(**self._kwargs)

    def fetch(self):
        params = values.of({})
        
        return self._version.fetch(
            EventInstance,
            self._kwargs,
            'GET',
            self._uri,
            params=params,
        )


class EventInstance(InstanceResource):

    def __init__(self, version, payload, workspace_sid, sid=None):
        super(EventInstance, self).__init__(version)
        
        # Marshaled Properties
        self._properties = {
            'account_sid': payload['account_sid'],
            'actor_sid': payload['actor_sid'],
            'actor_type': payload['actor_type'],
            'actor_url': payload['actor_url'],
            'description': payload['description'],
            'event_data': payload['event_data'],
            'event_date': deserialize.iso8601_datetime(payload['event_date']),
            'event_type': payload['event_type'],
            'resource_sid': payload['resource_sid'],
            'resource_type': payload['resource_type'],
            'resource_url': payload['resource_url'],
            'sid': payload['sid'],
            'source': payload['source'],
            'source_ip_address': payload['source_ip_address'],
            'url': payload['url'],
        }
        
        # Context
        self._lazy_context = None
        self._context_properties = {
            'workspace_sid': workspace_sid,
            'sid': sid or self._properties['sid'],
        }

    @property
    def _context(self):
        if self._lazy_context is None:
            self._lazy_context = EventContext(
                self._version,
                self._context_properties['workspace_sid'],
                self._context_properties['sid'],
            )
        return self._lazy_context

    @property
    def account_sid(self):
        """ The account_sid """
        return self._properties['account_sid']

    @property
    def actor_sid(self):
        """ The actor_sid """
        return self._properties['actor_sid']

    @property
    def actor_type(self):
        """ The actor_type """
        return self._properties['actor_type']

    @property
    def actor_url(self):
        """ The actor_url """
        return self._properties['actor_url']

    @property
    def description(self):
        """ The description """
        return self._properties['description']

    @property
    def event_data(self):
        """ The event_data """
        return self._properties['event_data']

    @property
    def event_date(self):
        """ The event_date """
        return self._properties['event_date']

    @property
    def event_type(self):
        """ The event_type """
        return self._properties['event_type']

    @property
    def resource_sid(self):
        """ The resource_sid """
        return self._properties['resource_sid']

    @property
    def resource_type(self):
        """ The resource_type """
        return self._properties['resource_type']

    @property
    def resource_url(self):
        """ The resource_url """
        return self._properties['resource_url']

    @property
    def sid(self):
        """ The sid """
        return self._properties['sid']

    @property
    def source(self):
        """ The source """
        return self._properties['source']

    @property
    def source_ip_address(self):
        """ The source_ip_address """
        return self._properties['source_ip_address']

    @property
    def url(self):
        """ The url """
        return self._properties['url']

    def fetch(self):
        self._context.fetch()