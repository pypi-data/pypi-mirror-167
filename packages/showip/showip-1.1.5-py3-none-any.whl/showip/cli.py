def main():
    try:
        from showip.showip import getdata, dns
    except ModuleNotFoundError:
        from showip import getdata, dns
    import argparse

    parser = argparse.ArgumentParser(description='Get information about your IP or any other IP')
    parser.add_argument('-ip', type=str, help='Enter IP to get information')
    args = parser.parse_args()

    data = getdata(args.ip)
    print(f'IP: {data["query"]}\nCountry: {data["country"]}, {data["countryCode"]}\nRegion: {data["regionName"]}, {data["region"]}\nCity: {data["city"]}\nISP: {data["isp"]}\nReverse: {data["reverse"]}')
    if args.ip == None:
        try:
            dns = dns()
            print("----------------------------")
            print(f"DNS: {dns['dns']['ip']}({dns['dns']['geo']})")
        except:
            print("Can't get DNS")
if __name__ == "__main__":
    main()