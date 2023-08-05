import json
import sys
import json
import requests


def do_cmd_getalerts(ops, args):
    if args.query:
        try:
            ops.validate_alert_query(args.query)
        except ValueError as e:
            print("\nERROR: %s" % (e))
            sys.exit(1)

    if args.count and not args.filter:
            print("Matched %i alerts." % (ops.get_alerts_count(args.query)))
    else:
        alerts = ops.get_alerts(args.query, 1, args.brief, args.descr, args.filter)
        if args.count:
            print("Matched %i alerts after post-filtering." % (len(alerts)))
        else:
            print(json.dumps(alerts, indent=2, sort_keys=False))

        if args.heal or args.action:
            for alert in alerts:
                if args.heal:
                    try:
                        print("Posted Ok for " + alert['uniqueId'] + ": " + json.dumps(ops.post_alert_bearer(ops.make_healing_alert(alert))))
                    except requests.exceptions.RequestException as e:
                        print(repr(e))
                    except Exception as e:
                        print("Unable to create heal alert for alert " + alert['uniqueId'])
                        print(repr(e))   
                if args.action == "Heal" or args.action == "acknowledge" or args.action == "suppress" or args.action ==  "close" or args.action ==  "unsuppress" or args.action == "unAcknowledge":
                    try:
                        print ("Result for " + alert['uniqueId'] + ": " + json.dumps(ops.do_alert_action(args.action, alert['uniqueId'])))
                    except requests.exceptions.RequestException as e:
                        print(repr(e))
                    except Exception as e:
                        print("Unable to perform action on alert " + alert['uniqueId'])
                        print(repr(e))        

def do_cmd_postalerts(ops, args):
    if args.auth == 'vtoken':
        post_alert = ops.post_alert_vtoken
    elif args.auth == 'oauth':
        post_alert = ops.post_alert_bearer
    else:
        raise Exception("Invalid auth type: %s.  Please use vtoken or oauth" % (args.auth))

    alerts = ops.get_json_from_file(args.infile)
    i=0
    for alert in alerts:
        if ops.is_in_range(args.range, i):
            print("Sending alert #" + str(i+1) + ":")
            print(post_alert(alert))
        i += 1