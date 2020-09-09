def SQ_Per (a):
    SQ = a ** 2
    return (SQ)

            
def SQ_Pe (a):
    Per = 4 * a
    return (Per)

a = int(input('Введите  сторону квадрата: '))
print ('Периметр  квадрата:',SQ_Per (a),'Площадь квадрата:',SQ_Pe (a))
