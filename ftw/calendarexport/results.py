from DateTime import DateTime
from Products.Five import BrowserView
from Products.CMFCore.utils import getToolByName
from Products.Five.browser.pagetemplatefile import ViewPageTemplateFile
from zope.component import getMultiAdapter


class CalendarExportResults(BrowserView):

    template = ViewPageTemplateFile('results.pt')

    def __call__(self):
        if self.request.form.get('export-events', '') == 'pdf':
            return getMultiAdapter((self.context, self.request),
                                   name=u'export_pdf')()
        elif self.request.form.get('export-events', '') == 'ical':
            return getMultiAdapter((self.context, self.request),
                                   name=u'export_ics')()
        return self.template()

    def events(self):
        """ Returns events searching 'from' and 'to' from request.
            If there are no data in request returns nothing.
        """
        catalog = getToolByName(self.context, 'portal_catalog')
        if self.request.form.get('from','') and self.request.form.get('to',''):
            start = DateTime(self.request.form.get('from','')).Date()
            end = DateTime(self.request.form.get('to','')).Date()
            return catalog(dict(
                portal_type='Event',
                start = {'range':'min', 'query': start},
                end = {'range':'max', 'query': end}))
        return

