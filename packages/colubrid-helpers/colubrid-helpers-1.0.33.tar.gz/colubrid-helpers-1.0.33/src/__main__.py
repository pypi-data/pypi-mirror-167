import os
import sys
import argparse
import subprocess
from pickle import TRUE
from .routestructure import routes_list
from .template import Imports, ImportsListroutes, ImportsController, ImportsSchemas



def migrate():
    subprocess.run(['alembic', 'upgrade', 'head'])

def makemigration(namemigration):
    subprocess.run(['alembic', 'revision', '--autogenerate', '-m', namemigration])

def updateListRute(listRoutes):
    with open(r'./routestructure.py', 'w') as fp:
        fp.write("%s\n" % "routes_list = [")
        for item in listRoutes:
            fp.write("\"%s\",\n" % item)
        fp.write("%s\n" % "]")

def create_route(route):
    if verify_create_route(route):
        create_route_structure(route)
        create_controller_structure(route)
        create_schema_structure(route)
        create_helper_structure(route)
        create_documentation_structure(route)
        create_routes_list()
        print("creating route, "+route)
    else:
        print("the route "+route+" has not been created")
        
def remove_route(route):
    if verify_remove_route(route):
        remove_route_structure(route)
        create_routes_list()
        print("Route "+route+" removed correctly!!!")
        
def create_route_structure(route):
    with open('endPoints/'+route+'_endpoint.py', 'w') as fp:
        fp.write(Imports)
        fp.write("from controllers import "+route+"_controller as "+route+"_controller \n\n")
        fp.write("from documentation import "+route+"_doc\n\n")
        fp.write("#region CRUD "+route+"\n")
        for crud in ['create', 'read', 'update', 'delete']:
            fp.write('@router.post("/'+crud+'/",tags=["Endpoint '+route+'"], summary='+route+'_doc.summary_'+crud+', description='+route+'_doc.description_'+crud+')\n')
            fp.write('def root(request: Request, db: Session = Depends(get_db)):\n\treturn '+route+'_controller.'+crud+'_'+route+'(db, request)\n\n')
        fp.write("#endregion\n\n\n")

def create_schema_structure(route):
    with open('schemas/'+route+'_schema.py', 'w') as fp:
        fp.write(ImportsSchemas)
        fp.write('class response_route(BaseModel):\n\tok: bool\n\tmessage: str\n')

def create_helper_structure(route):
    with open('helpers/'+route+'_helper.py', 'w') as fp:
        fp.write('# Your helpers here ')

def create_documentation_structure(route):
    with open('documentation/'+route+'_doc.py', 'w') as fp:
        fp.write('summary_create = "Create a new '+route+'"\n')
        fp.write('description_create = "Create a new '+route+' from route '+route+'/create "\n\n')
        fp.write('summary_read = "Read '+route+'"\n')
        fp.write('description_read = "Read '+route+' from route '+route+'/read and return a '+route+' list "\n\n')
        fp.write('summary_update = "Update '+route+'"\n')
        fp.write('description_update = "Update a register in '+route+' from route '+route+'/update "\n\n')
        fp.write('summary_delete = "Delete '+route+'"\n')
        fp.write('description_delete = "Delete a register in '+route+' from route '+route+'/delete "\n\n')

def create_controller_structure(route):
    with open('controllers/'+route+'_controller.py', 'w') as fp:
        fp.write(ImportsController)
        fp.write("from schemas."+route+"_schema import response_route \n")
        fp.write("\n#region CRUD "+route+"")
        for crud in ['create', 'read', 'update', 'delete']:
            fp.write('\ndef '+crud+'_'+route+'(db: Session, request):\n\treturn response_route(ok=True,message="Message from route '+route+'/'+crud+' ")\n')
        fp.write("#endregion\n\n\n")

def remove_route_structure(route):
    os.remove("endPoints/"+route+"_endpoint.py")
    os.remove("controllers/"+route+"_controller.py")
    os.remove("schemas/"+route+"_schema.py")
    os.remove("helpers/"+route+"_helper.py")
    os.remove("documentation/"+route+"_doc.py")


def create_routes_list():
    with open('routers/modules_routes.py', 'w') as fp:
        fp.write(ImportsListroutes)
        for r in routes_list:
            fp.write("from endPoints import "+r+"_endpoint\n")   
        fp.write("\nendPointsRoutes = APIRouter()\n\n")   
        for r in routes_list:
            fp.write('endPointsRoutes.include_router('+r+'_endpoint.router, include_in_schema=True, prefix="/'+r+'", tags=["Endpoint '+r+'"])\n')
       
        
def verify_create_route(route):
    question = False
    for r in routes_list:
        if r == route:
            question = True
            continue
    if question:
        try:
            yes = 'yes'
            y = 'y'
            Yes = 'Yes'
            YES = 'YES'
            verify = str(input("Error: route "+ route + " already exists!, do you want override it? (Yes/No) "))
        except Exception as e:
            verify = False
        if verify == 'yes' or verify == 'YES' or verify == 'Yes' or verify == 'y':
            return True  
        else:
            return False
    routes_list.append(route)
    updateListRute(routes_list)
    return True

def verify_remove_route(route):
    question = False
    for r in routes_list:
        if r == route:
            question = True
            continue
    if question:
        try:
            yes = 'yes'
            y = 'y'
            Yes = 'Yes'
            YES = 'YES'
            verify = str(input("Do you want remove route "+ route + "? (Yes/No) "))
        except Exception as e:
            verify = False
        if verify == 'yes' or verify == 'YES' or verify == 'Yes' or verify == 'y':
            routes_list.remove(route)
            updateListRute(routes_list)
            return TRUE
        else:
            return False
    print("Error: Route "+route+" does'n exists.")
       
    routes_list.remove



def options_command(argument):
    args = argument
    for arg in vars(argument):
        if getattr(args, arg) is not None:
            
            if arg == "route" or arg == "r":
                create_route(getattr(args, arg))
            if arg == "remove_route" or arg == "rm-r":
                remove_route(getattr(args, arg))     
            if arg == "makemigration":
                makemigration(getattr(args, arg))
            if arg == "migrate":
                migrate()
   
def main(args=None):
    parser = argparse.ArgumentParser(description='FastApi Multitenant.')
    parser.add_argument("--route", help="Crete new route.")
    parser.add_argument("--r", help="Crete new route.")
    parser.add_argument("--remove-route", help="Remove route.")
    parser.add_argument("--rm-r", help="Remove route.")
    parser.add_argument("--migrate", help="Migarte.", nargs='?', const=1, type=int)
    parser.add_argument("--makemigration", help="Migarte.")
    args = parser.parse_args()
    options_command(args)

if __name__ == "__main__":
    sys.exit(main())
     


