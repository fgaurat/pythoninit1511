import traceback

def div(a,b):
    
        c = a/b
        return c

def call_div(a,b):
    print('call_div')
    try:
        c = div(a,b)
        return c
    # except Exception as e:
    #     print(e)
    #     raise e
    finally:
        print("le traitement")


def main():
    try:
        a=2
        b=int(input("b : "))
        c = call_div(a,b)
        print("main c :",c)
    except ZeroDivisionError as e:
        print("erreur !")
        print(e)
        traceback.print_exc()
    except ValueError as e:
        print('ValueError',e)
    
    except Exception as e:
        print(e)
    
    print("la suite")
if __name__ == '__main__':
    main()