import json
import subprocess

cmd = subprocess.run(['osascript', '-e', 'tell application "Bunch Beta" to list open bunches'], capture_output=True)
# cmd=subprocess.run(['ruby', 'bunch.rb', '-l'], capture_output=True)
items=cmd.stdout.decode('utf-8')

def make_json_path(p):
    return {
        "title": p,
        "subtitle": "close the Bunch ‘{}’".format(p),
        "arg": p,
        }

if len(items) > 2:
    json_item = {}
    bunch_items = [x for x in items.split(', ') if x]
    json_item['items']=list(map(make_json_path, bunch_items))
    print(json.dumps(json_item))
