import view, export, importdata



def Start():
    value = view.UserValue()

    if value == 1:
        export.ExportValues(view.UserInformation())
    elif value == 2:
        importdata.ImportValues()
    elif value == 3:
        filter = view.UsingFilter()
        if filter == 1:
            importdata.ImportFilter(0)
        else:
            importdata.ImportFilter(1)
    elif value == 4:
        importdata.ImportFio()

