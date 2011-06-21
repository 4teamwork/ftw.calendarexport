from Products.CMFCore.utils import getToolByName
from Products.Five.browser.pagetemplatefile import ViewPageTemplateFile
from plone.app.layout.viewlets import ViewletBase


class ExportEvents(ViewletBase):
    render = ViewPageTemplateFile('export.pt')
    
    def active(self):
        props = getToolByName(self.context, 'portal_properties').calendarexport_properties
        return props.getProperty('active')
