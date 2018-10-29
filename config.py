import click
from utils import create_config_file


@click.command()
@click.option('--clistloginemail', prompt="Craigslist Login Email", default="")
@click.option('--clistloginpassword', prompt='Craigslist Password', hide_input=True, confirmation_prompt=True,
              default="")
@click.option('--contactnumber', prompt='Contact Number', default="")
@click.option('--contactname', prompt='Contact Name', default="")
@click.option('--posttitle', prompt='Post Title')
@click.option('--postcode', prompt='Zip Code')
@click.option('--postcontent', prompt='Post Content')
@click.option('--price', prompt='Price')
@click.option('--odometer', prompt='Odometer Reading', default="")
@click.option('--vin', prompt='VIN', required=False, default="")
@click.option('--condition', prompt='Condition', default="")
@click.option('--cylinders', prompt='Cylinders (2,4,6,8)', default="")
@click.option('--fuel', prompt='Fuel Type', default="")
@click.option('--drive', prompt='Drive Type', default="")
@click.option('--color', prompt='Color', default="")
@click.option('--size', prompt='Size', default="")
@click.option('--transmission', prompt='Transmission Type')
@click.option('--titlestatus', prompt='Title Status')
@click.option('--cartype', prompt='Car Type', default="")
@click.option('--modelyear', prompt='Model Year', default="")
@click.option('--makeandmodel', prompt='Make and Model')
def configure(clistloginemail, clistloginpassword, contactnumber, contactname, posttitle, postcontent, postcode, price,
              odometer, vin, condition, cylinders, fuel, drive, color, size, transmission, titlestatus, cartype,
              modelyear, makeandmodel):
    create_config_file({
        'clistLoginEmail': clistloginemail,
        'clistLoginPassword': clistloginpassword,
        'contactNumber': contactnumber,
        'contactName': contactname,
        'postTitle': posttitle,
        'postCode': postcode,
        'price': price,
        'postContent': postcontent,
        'odometer': odometer,
        'vin': vin,
        'condition': condition,
        'cylinders': cylinders,
        'fuel': fuel,
        'drive': drive,
        'color': color,
        'size': size,
        'transmission': transmission,
        'titleStatus': titlestatus,
        'carType': cartype,
        'modelYear': modelyear,
        'makeAndModel': makeandmodel
    })


def setupConfig(clistloginemail, clistloginpassword):
    click.echo('User is: %s' % clistloginemail)
