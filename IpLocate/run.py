from paramSeeker.seeker import ParamSeeker
from IpLocate import IpLocate, __version__, left_space

app = ParamSeeker()
app.set_desc("""little tool to get location by the HOST or the IP""")


@app.seek(extra={'default': '127.0.0.1'})
def my_ip(wanted):
    ip_addr = IpLocate()
    if wanted == '127.0.0.1':
        result = ip_addr.my_locate()
    else:
        if ':' in wanted or wanted.split('.')[-1].isdigit():
            ip_addr.ip = wanted
        else:
            ip_addr.host = wanted
        result = ip_addr.his_locate()
    container = "\n{}\033[01;32m{}\033[00m\n\n".format(5 * ' ', result.get('ip', '0.0.0.0'))
    container += "LAT/LON{}{}\n".format(left_space('LAT/LON', 20) * ' ', result.get('loc', 'unable to retrieve'))
    if 'country' in result:
        container += 'Country{}{}\n'.format(left_space('country', 20) * ' ', result['country'])
    if 'region' in result:
        container += 'Region{}{}\n'.format(left_space('region', 20) * ' ', result['region'])
    if 'city' in result:
        container += 'City{}{}\n'.format(left_space('city', 20) * ' ', result['city'])
    if 'hostname' in result and not result['hostname'] == 'No Hostname':
        container += 'Hostname{}{}\n'.format(left_space('hostname', 20) * ' ', result['hostname'])
    if 'postal' in result:
        container += 'Postal Code{}{}\n'.format(left_space('Postal Code', 20) * ' ', result['postal'])
    if 'org' in result:
        container += 'Network{}{}\n'.format(left_space('Network', 20) * ' ', result['org'])
    if 'phone' in result:
        container += 'Phone Number{}{}\n'.format(left_space('Phone Number', 20) * ' ', result['phone'])
    return container


@app.seek('--version', short='-v', is_mark=True, extra={'desc': 'version info'})
def show_version(wanted):
    print('v' + __version__)
    exit(0)


app.set_usage_desc('iplocate')
app.set_usage_desc('iplocate ip')
app.set_usage_desc('iplocate hostname')


def main():
    app.run()


if __name__ == '__main__':
    main()

