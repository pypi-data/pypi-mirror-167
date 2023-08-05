import re, json,os
import argparse
from argparse import RawTextHelpFormatter

def ParseData (Data, RegexArray):
    result = {}
    for Regex in RegexArray['All']:
        search = re.search(Regex,Data)
        if search:
            result.update(search.groupdict())
    if RegexArray['Conditional']:
        try:
            Regexes = RegexArray['Conditional']['Conditions'][result[RegexArray['Conditional']['ConditionField']]]
            for regex in Regexes:
                search = re.search(RegexArray['Conditional']['Regexes'][regex],result[RegexArray['Conditional']['ParseField']])
                if search:
                    result.update(search.groupdict())
        except:
            None
    return json.dumps(result,indent=4)
def Optm_ParserEngine(Parsername,Data):
    f = open(os.path.join(os.path.dirname(os.path.abspath(__file__)),'Config.json'))
    Config = json.load(f)
    f.close()
    return ParseData(Data,Config['regex'][Parsername])
def ShowParser():
    f = open(os.path.join(os.path.dirname(os.path.abspath(__file__)),'Config.json'))
    Config = json.load(f)
    f.close()
    return Config['Parser']

def PossibleRegex(data,Parsername):
    f = open(os.path.join(os.path.dirname(os.path.abspath(__file__)),'Config.json'))
    Config = json.load(f)
    f.close()
    regexes = Config['regex'][Parsername]['Conditional']['Regexes']
    for reg in regexes.keys():
        search = re.search(regexes[reg],data)
        if search:
            print(f'Extraction for {reg}: ',search.groupdict())

            

def main():
    Description = '''
# Optimized Parser Engine

    '''
    arguments = argparse.ArgumentParser(description=Description,usage="%(prog)s [options] [parameter]",formatter_class=RawTextHelpFormatter)
    arguments.add_argument('Options',metavar='Options',choices=['Show','Parse','Test'],help='Option for command line: \nShow\nParse\nTest',type=str)
    arguments.add_argument('-p',dest='parser',choices=ShowParser(),help='Provide the parser groupname contains your regex. Possible Values',required=)
    arguments.add_argument('-d',dest='data',help='Provide the data which you want to parse',required=False)
    

    args = arguments.parse_args()
    if args.Options == 'Parse':
        if args.parser and args.data:
            print(Optm_ParserEngine(args.parser,args.data))
        else:
            print("-p and -d argument should have value")
    elif args.Options == 'Show':
        print('\n'.join(ShowParser()))
    elif args.Options == 'Test':
        if args.parser and args.data:
            print(PossibleRegex(args.data,args.parser))
        else:
            print("-p and -d argument should have value")