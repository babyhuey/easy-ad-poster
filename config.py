import click
from utils import create_config_file


@click.command()
@click.option('--clistloginemail', prompt="Craigslist Login Email")
@click.option('--clistloginpassword', prompt='Craigslist Password', hide_input=True, confirmation_prompt=True)
@click.option('--contactnumber', prompt='Contact Number')
@click.option('--contactname', prompt='Contact Name')
@click.option('--posttitle', prompt='Post Title', required=True)
@click.option('--postcode', prompt='Zip Code', required=True)
@click.option('--postcontent', prompt='Post Content')
@click.option('--price', prompt='Auction Price')
@click.option('--odometer', prompt='Odometer Reading')
@click.option('--vin', prompt='VIN', required=False)
@click.option('--condition', prompt='Condition')
@click.option('--cylinders', prompt='Cylinders (2,4,6,8)')
@click.option('--fuel', prompt='Fuel Type')
@click.option('--drive', prompt='Drive Type')
@click.option('--color', prompt='Color')
@click.option('--size', prompt='Size')
@click.option('--transmission', prompt='Transmission Type')
@click.option('--titlestatus', prompt='Title Status')
@click.option('--cartype', prompt='Car Type')
@click.option('--modelyear', prompt='Model Year')
@click.option('--makeandmodel', prompt='Make and Model')
def configure(clistloginemail, clistloginpassword, contactnumber, contactname, posttitle, postcontent, postcode, price,
                       odometer, vin, condition, cylinders, fuel, drive, color, size, transmission, titlestatus,
                       cartype, modelyear, makeandmodel):
    create_config_file({
        'clistLoginEmail': clistloginemail,
        'clistLoginPassword': clistloginpassword,
        'contactNumber': contactnumber,
        'contactName': contactname,
        'postTitle': posttitle,
        'postCode': postcode,
        'price': price,
        'postContent':postcontent,
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



