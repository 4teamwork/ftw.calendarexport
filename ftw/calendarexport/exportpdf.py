from Products.Five.browser import BrowserView
from event_layout import EventLayout

class ExportPDFView(BrowserView):

    def __call__(self):
        arguments = {
            'default_book_settings' : False,
            'pre_compiler': pre_compiler,
        }
        as_pdf = self.context.restrictedTraverse(
            '%s/as_pdf' % '/'.join(self.context.getPhysicalPath())
        )
        return as_pdf(**arguments)

def pre_compiler(view, object):
    layout = EventLayout()
    layout(view, object)