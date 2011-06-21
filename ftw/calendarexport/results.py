from DateTime import DateTime
from Products.Five import BrowserView
from Products.CMFCore.utils import getToolByName
from Products.Five.browser.pagetemplatefile import ViewPageTemplateFile


class CalendarExportResults(BrowserView):

    template = ViewPageTemplateFile('results.pt')

    def __call__(self):
        if self.request.form.get('export-events', '') == 'pdf':
            return self.export_pdf(self.request.form.get('uids', []))
        elif self.request.form.get('export-events', '') == 'ical':
            return self.export_ical(self.request.form.get('uids', []))
        return self.template()

    def events(self, uids=[]):
        """ Returns events searching 'from' and 'to' from request.
            If there is the argument 'uids' the request is ignored.
            If there are no 'uids' and no data in request returns nothing.
        """
        catalog = getToolByName(self.context, 'portal_catalog')
        if uids:
            return catalog({'uid': uids})
        if self.request.form.get('from','') and self.request.form.get('to',''):
            start = DateTime(self.request.form.get('from','')).Date()
            end = DateTime(self.request.form.get('to','')).Date()
            return catalog(dict(
                portal_type='Event',
                start = {'range':'min', 'query': start},
                end = {'range':'max', 'query': end}))
        return

    def export_ical(self, uids):
        """
        """
        events = self.events(uids=uids)
        return 'ical\n====\n %s' % '\n'.join(uids)

    def export_pdf(self, uids):
        """
        """
        events = self.events(uids=uids)
        return 'pdf\n===\n%s' % '\n'.join(uids)
