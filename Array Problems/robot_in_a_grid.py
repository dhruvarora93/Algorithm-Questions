def getPath(maze,rows,columns,path,failedpoints):
    if(rows<0 or columns<0 or not maze[rows][columns]):
        return False
    point=(rows,columns)

    if point in failedpoints:
        return False

    isorigin = rows == 0 and columns == 0

    if(isorigin or getPath(maze,rows-1,columns,path,failedpoints) or getPath(maze,rows,columns-1,path,failedpoints)):
        path.append(point)
        return True


    failedpoints.append(point)
    return False




