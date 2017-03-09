import os

from control_values.crc import crc
from control_values.ean_13 import ean_13
from control_values.ecc import ecc_control_sum, restore_message
from control_values.itn import itn
from control_values.luhn import luhn
from control_values.odd_even_bit import odd_even
from control_values.railway import railway
from report.jinja_settings import render_template


OUT_DIR = 'out'
TEMP_FILE = 'report.tex'
OUT_FILE = 'report.pdf'


def show_report(template, context, out_dir=OUT_DIR, tex_file=TEMP_FILE, pdf_file=OUT_FILE):
    tex = render_template(template, context)
    if not os.path.exists(out_dir):
        os.makedirs(out_dir)
    os.chdir(out_dir)
    with open(tex_file, 'w+') as f:
        f.write(tex)
    os.system('pdflatex {} > /dev/null'.format(tex_file))
    os.system('evince {} > /dev/null'.format(pdf_file))


if __name__ == '__main__':

    message = 'Федосеев'
    context = {
        'func': {
            'str': str
        },
        'odd_even': odd_even(message),
        'luhn': luhn(message),
        'ean_13': ean_13(message),
        'itn': itn(message),
        'railway': railway(message),
        'ecc': ecc_control_sum(message),
        'ecc_err_0': restore_message(message, 0),
        'ecc_err_1': restore_message(message, 1),
        'ecc_err_2': restore_message(message, 2),
        'crc': crc(message[:3]),
    }
    show_report('templates/main.tex', context)
