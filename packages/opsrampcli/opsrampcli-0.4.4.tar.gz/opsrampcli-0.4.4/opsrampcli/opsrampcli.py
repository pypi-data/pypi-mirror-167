import json
from opsrampcli import argparsing, opsrampenv, alerts, incidents, resources, discovery, escalationpolicies, customattrs, servicemaps

def main():
    args = argparsing.do_arg_parsing()  
    ops = None
    if hasattr(args, "env"):
        ops = opsrampenv.OpsRampEnv(args.env, args.envfile, args.secure)

    if args.command == "getalerts":
        alerts.do_cmd_getalerts(ops, args)
    elif args.command == "postalerts":
        alerts.do_cmd_postalerts(ops, args)
    elif args.command == "getincidents":
        incidents.do_cmd_getincidents(ops, args)
    elif args.command == "getdiscoprofile":
        discovery.do_cmd_getdiscoprofile(ops, args)
    elif args.command == "getalertesc":
        escalationpolicies.do_cmd_getalertescalations(ops, args)
    elif args.command == "migratealertesc":
        escalationpolicies.do_cmd_migratealertescalations(ops, args)
    elif args.command == "getcustomattrs":
        customattrs.do_cmd_get_custom_attributes(ops, args)
    elif args.command == "getresources":
        resources.do_cmd_get_resources(ops, args)
    elif args.command == "exportcustattrfile":
        customattrs.do_cmd_make_custom_attr_file(ops, args)
    elif args.command == "importcustattrfile":
        customattrs.do_cmd_import_custom_attr_file(ops, args)
    elif args.command == "getservicemaps":
        print(json.dumps(ops.get_service_maps(), indent=2, sort_keys=False));
    elif args.command == "getchildsvcgroups":
        print(json.dumps(ops.get_child_service_groups(args.parent), indent=2, sort_keys=False));
    elif args.command == "getservicegroup":
        print(json.dumps(ops.get_service_group(args.id), indent=2, sort_keys=False));
    elif args.command == "exportservicemaps":
        servicemaps.do_cmd_export_service_maps(ops, args)
    elif args.command == "transformsvcmap":
        servicemaps.do_cmd_transform_service_map(args)
    elif args.command == "importservicemaps":
        servicemaps.do_cmd_import_service_maps(ops, args)
    elif args.command == "cloneservicemaps":
        servicemaps.do_cmd_clone_service_maps(ops, args)
if __name__ == "__main__":
    main()
