from ipykernel.kernelbase import Kernel
import json
import requests
import logging

__version__ = '0.2.0'

api_base = 'http://localhost:61494/'
api_run = 'code/run'
api_defs = 'api/definitions'

def load_definitions():
    return json.loads(requests.get(api_base + api_defs, verify=False).text)

class LithiumKernel(Kernel):
    implementation = 'Lithium'
    implementation_version = __version__
    language = 'lithium-lisp'
    language_version = '2022.8.31.1105'
    language_info = {
        'name': 'Lithium LISP',
        'mimetype': 'application/x-lisp',
        'file_extension': '.lsp',
    }
    banner = "Lithium LISP - programming language for ReLife Platform"

    def run_code(self, module, code):
        try:
            js = {'module':module, 'code':code}
            res = json.loads(requests.post(api_base + api_run, json=js, verify=False).text)

            if res['download'] is not None:
                ht = requests.get(res['download'], verify=False).text
                return self.send_html(ht, res['redirect'])
            else:
                return self.send_plain(res['result'])
        except Exception as e:
            logging.error(e)

    def send_html(self, h, l):
        self.send_response(self.iopub_socket, 'display_data', {
            'data': {
                'text/html': '<a href="{}">View via host</a><br/>'.format(l) + h,
                'text/plain': l
            },
            'metadata': {}
        })

    def send_plain(self, r):
        self.send_response(self.iopub_socket, 'execute_result', {
            'data': {
                'text/plain': str(r)
            },
            'execution_count': self.execution_count,
            'metadata':{}
        })

    def do_execute(self, code, silent, store_history=True, user_expressions=None, allow_stdin=False):
        if not silent:
            self.run_code('t', code)

        return {
            'status': 'ok',
            'execution_count': self.execution_count,
            'payload': [],
            'user_expressions': {}
        }