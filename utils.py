
def convert_bytes(bytes):
    """Returns a human readable string of the target bytes
    @remark used with os.path.getsize(...)
    """
    if not bytes:
        return '??'
    bytes = float(bytes)
    if bytes >= 1099511627776:
        terabytes = bytes / 1099511627776
        size = '%.2fT' % terabytes
    elif bytes >= 1073741824:
        gigabytes = bytes / 1073741824
        size = '%.2fG' % gigabytes
    elif bytes >= 1048576:
        megabytes = bytes / 1048576
        size = '%.2fM' % megabytes
    elif bytes >= 1024:
        kilobytes = bytes / 1024
        size = '%.2fK' % kilobytes
    else:
        size = '%.2fb' % bytes
    return size
    
    
def format_number(number, prepend=None):
    """Returns a formatted number string
    """
    isNeg = (number < 0)
    if isNeg:
        number = (number * -1) # abs value

    numString = str(number)
    nLen = len(numString)
    precision = None

    # strip off the decimal precision
    if numString.find(".") >= 0:
        components = numString.split(".")
        numString = components[0]
        precision = components[1]
        # add the trailing zero, if needed
        if len(precision) == 1:
            precision = precision+"0" 
        elif len(precision) > 2:
            precision = precision[:2]
        pass
        
    numGroup = [ ]
    numList = list(numString)
    numList.reverse()
    
    # aggregate the groups
    for nGroup in range(0, nLen):
        n = (nGroup * 3)
        grp = numList[n:(n + 3)]
        if grp:
            grp.reverse()
            numGroup.append(grp)
        pass
        
    # build the string
    numGroup.reverse()
    tmpGroup = ["".join(g) for g in numGroup]
    tmpString = ",".join(tmpGroup)
    if precision:
        tmpString += "."+precision
    if isNeg:
        tmpString = "-"+tmpString
    if prepend:
        tmpString = prepend+tmpString
    return tmpString
    
    
def get_percent(num1, num2, format=True):
    """Returns the percent of num1
    @remark: num1 (smaller num) / num2 (larger num)
    """   
    percent = 0.0
    try:
        percent = ((float(num2) - float(num1)) / float(num2)) * 100
    except ZeroDivisionError:
        pass
        
    if format:
        return "%.2f%%" % percent

    return percent
