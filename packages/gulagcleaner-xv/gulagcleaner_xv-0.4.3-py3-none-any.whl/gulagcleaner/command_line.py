from gulagcleaner import gulagcleaner_extract
from os.path import exists

# def common_member(a, b):
#     a_set = set(a)
#     b_set = set(b)
#     if (a_set & b_set):
#         return True 
#     else:
#         return False

def main():
    '''
    Main function called from the "gulagcleaner" CLI command.
    The gulagcleaner command takes an argv for the path and tries to deembed the pages inside it.
    The pages are saved in a new PDF in the same folder.
    '''
    
    import sys
    opt = ['-r']
    if len(sys.argv)>1:
        if '-r' in sys.argv:
            replace = True
            sys.argv.remove('-r')
        del sys.argv[0]
        for arg in sys.argv:
            if exists(arg):
                return_msg=gulagcleaner_extract.deembed(arg,replace)
                
                if return_msg["Success"]:
                    print("Deembedding successful. File saved in",return_msg["return_path"])
                    print("Metadata:")
                    print("Archivo: "+return_msg["Meta"]["Archivo"])
                    print("Autor: "+return_msg["Meta"]["Autor"])
                    print("Asignatura: "+return_msg["Meta"]["Asignatura"])
                    print("Curso y Grado: "+return_msg["Meta"]["Curso y Grado"])
                    print("Facultad: "+return_msg["Meta"]["Facultad"])
                    print("Universidad: "+return_msg["Meta"]["Universidad"])
                    
                else:
                    print("Error:",return_msg["Error"])
            else:
                print("File not found.")
        else:
            pass
    else:
        print('Usage: gulagcleaner "filename"')
    
if __name__ == "__main__":
    print('Call from the "gulagcleaner" command.')
