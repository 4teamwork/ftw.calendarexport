class EventLayout(object):
    
    def __call__(self, view, context):
        self.view = view
        self.context = context
        self.setDocumentClass()
        self.registerPackages()
        self.appendHeadCommands()
        self.appendAboveBodyCommands()
        self.appendBeneathBodyCommands()
        
    def setDocumentClass(self):
        self.view.setLatexProperty('document_class', 'letter')
        self.view.setLatexProperty('document_config', 'a4paper,10pt,german')

    def registerPackages(self):
        self.view.registerPackage('ae,aecompl')
        self.view.registerPackage('geometry', 'left=20mm,right=20mm,top=25mm,bottom=30mm')
        self.view.registerPackage('babel','ngerman')
        self.view.registerPackage('textpos','absolute, overlay')
        self.view.registerPackage('textcomp')
        self.view.registerPackage('longtable')
        self.view.registerPackage('lmodern')
        self.view.registerPackage('fontenc', 'T1')
        self.view.registerPackage('inputenc', 'utf8')

    def appendHeadCommands(self):
        self.view.appendHeaderCommand(r'\renewcommand{\familydefault}{bng}')
        self.view.appendHeaderCommand(r'\renewcommand*\familydefault{\sfdefault}')
        self.view.appendToProperty('latex_above_body', r'\pagestyle{empty}')

    def appendAboveBodyCommands(self):
        pass

    def appendBeneathBodyCommands(self):
        pass
        #self.view.appendToProperty('latex_beneath_body', r'')
        
