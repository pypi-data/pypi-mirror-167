import os
import sys
import time
import requests
import argparse
import concurrent.futures
from bs4 import BeautifulSoup as bs


def show_results(results, first=False):
    temp = [None for _ in range(len(results))]
    for index, result in enumerate(results):
        if result == 'EMPTY@#@':
            temp[index] = f'Test {index+1}'
        elif result == 'ERROR!@!':
            temp[index] = f'Test {index+1} \033[31m Timeout \033[0m'
        else:
            temp[index] = f'Test {index+1} {result}'

    if not first:
        for _ in range(len(results)):
            print('\033[1A', end='\x1b[2K')
    print('\n'.join(temp))


def main():
# if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('-p', '--processor', type=int, default=4, help='number of processor to grade algorithm samples')
    parser.add_argument('-n', '--name', type=str, default='', help='name of python script having URL and solution funciton')
    parser.add_argument('-c', '--create', type=str, default='', help='create a template file for solving algorithm')
    args = parser.parse_args()
    
    if not args.name and not args.create:
        print('Please grade a solution or create a new file for solving algorithm.')
        sys.exit()

    if args.create:
        args.create = args.create if args.create[-3:] == '.py' else args.create + '.py'
        if args.create in os.listdir(os.getcwd()):
            print('The file already exists.')
            sys.exit()

        file_content = """# Do not modify name of parameter and function ('URL', 'solution')
URL = ''

# input_data: sample input
def solution(input_data):
    answer = 0

    return answer
        """
        with open(args.create, 'w') as f:
            f.write(file_content)
        
        sys.exit()

    if args.name:
        try:
            args.name = args.name.split('.')[0] if '.py' in args.name else args.name
            solution = __import__(args.name)
        except:
            print(f'There is no {args.name} file in here.')
            sys.exit()
        
        try:
            URL = solution.URL
        except:
            print(f'The solution file dose not correspond.')
            sys.exit()
        
        if 'acmicpc' not in URL:
            print('URL is not from baekjoon algorithm site.')
            sys.exit()

        try:
            res = requests.get(URL)
        except requests.exceptions.ConnectionError:
            print('Check the internet connection.')
            sys.exit()

        soup = bs(res.text, 'html.parser')

        start_idx = 1
        inputs = []
        outputs = []
        while len(soup.select(f'#sample-input-{start_idx}')) != 0:
            input_data = soup.select(f'#sample-input-{start_idx}')[0].text
            output_data = soup.select(f'#sample-output-{start_idx}')[0].text
            inputs.append(input_data)
            outputs.append(output_data)

            start_idx += 1
        
        results = ['EMPTY@#@' for _ in range(len(inputs))]
        show_results(results, first=True)
        with concurrent.futures.ProcessPoolExecutor() as executor:
            for sample_index, (input_data, output_data) in enumerate(zip(inputs, outputs), 1):
                start = time.time()
                future = executor.submit(solution.solution, input_data)
                try:
                    result = future.result(timeout=10)
                    result = '\033[32m PASS \033[0m' if output_data == result else '\033[31m FAIL \033[0m'
                    result += f'   {time.time()-start:.2f} (s)'
                    results[sample_index-1] = result
                    show_results(results)
                except concurrent.futures.TimeoutError:
                    future.cancel()
                    result = 'ERROR!@!'
                    results[sample_index-1] = result
                    show_results(results)