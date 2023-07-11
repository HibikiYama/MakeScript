import numpy as np
import csv

def MakeScriptName():
    print('New script name is ...')
    name = input('Enter:')
    print('')
    return name

def AddScriptName():
    print('Script name is ...')
    name = input('Enter:')
    print('')
    return name

def YesNo():
    yesno = input('Enter:')
    return yesno

def AddPriority():
    print('Priority is ...')
    Priority = input('Enter:')
    print('')
    return Priority

def AddBlockID():
    print('BlockID is ...')
    BlockID = input('Enter:')
    print('')
    return BlockID

def AddObserver():
    print('Observer is ...')
    Observer = input('Enter:')
    print('')
    return Observer

def AddObjectName():
    print('ObjectName is ...')
    ObjectName = input('Enter:')
    print('')
    return ObjectName

def AddObjectType():
    print('ObjectType is ...')
    ObjectType = input('Enter:')
    print('')
    return ObjectType

def AddRA():
    print('RA is ...')
    RA = input('Enter:')
    print('')
    return RA

def AddDEC():
    print('DEC is ...')
    DEC = input('Enter:')
    print('')
    return DEC

def AddRAoffset():
    print('RAoffset is ...')
    RAoffset = input('Enter:')
    print('')
    return RAoffset

def AddDECoffset():
    print('DECoffset is ...')
    DECoffset = input('Enter:')
    print('')
    return DECoffset

def AddROToffset():
    print('ROToffset is ...')
    ROToffset = input('Enter')
    print('')
    return ROToffset

def AddFilter1():
    print('Filter1 is ...')
    Filter1 = input('Enter:')
    print('')
    return Filter1

def AddFilter2():
    print('Filter2 is ...')
    Filter2 = input('Enter:')
    print('')
    return Filter2

def AddDitherType():
    print('DitherType is ...')
    DitherType = input('Enter:')
    print('')
    return DitherType

def AddDitherRadius():
    print('DitherRadius is ...')
    while True:
        DitherRadius = input('Enter:')
        if int(DitherRadius) >=0:
            print('')
            break;
        else :
            print('Please set a value greater than or equal to 0.')
            continue;
    return DitherRadius

def AddDitherPhase():
    print('DitherPhase is ...')
    while True:
        DitherPhase = input('Enter:')
        if int(DitherPhase) > 0:
            print('')
            break;
        else :
            print('Please set a value greater than or equal to 1.')
            continue;
    return DitherPhase

def AddDitherTotal():
    print('DitherTotal is ...')
    while True:
        DitherTotal = input('Enter:')
        if int(DitherTotal) > 0:
            print('')
            break;
        else :
            print('Please set a value greater than or equal to 1.')
            continue;
    return DitherTotal

def AddImages():
    print('Images is ...')
    while True:
        Images = input('Enter:')
        if int(Images) > 0:
            print('')
            break;
        else :
            print('Please set a value greater than or equal to 1.')
            continue;
    return Images

def AddIntegrationTime():
    print('IntegrationTime is ...')
    while True:
        IntegrationTime = input('Enter:')
        if int(IntegrationTime) > 0:
            print('')
            break;
        else :
            print('Please set a value greater than or equal to 1.')
            continue;
    return IntegrationTime

def AddComment1():
    print('Comment1 is ...')
    Comment1 = input('Enter:')
    print('')
    return Comment1

def AddComment2():
    print('Comment2 is ...')
    Comment2 = input('Enter:')
    print('')
    return Comment2
