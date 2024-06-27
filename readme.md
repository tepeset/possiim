Project Outline:
    Point of Sale System:
        A system that can request pricing info and descriptions from a database, calculate the totals, add tax etc., process payment, and present a reciept of the transaction
        with areas for notes, customer information, and follow up instructions or information for the customer as well. This would also update the database to reflect the new
        inventory numbers, so that inventory could be accurate. Quotes should be available through this interface as well, to provide advanced notice to customers seeking 
        information, or comparison shopping before committing. 

    Inventory System:
        A system to input data into the database for very detailed information on a product for resale.
            Data to be Input:
                ITEM NAME:  
                    The short description to appear on the receipt/quote, that is easily understood by all parties involved
                ITEM DESCRIPTION:
                    A more detailed description of the item, to help compare between similar items, or to help source this specific item from different vendors. May include
                    specific product numbers, dimensions, or other detailed descriptors, along with any additional information for ordering, inventory, or other general
                    knowledge purposes. Will not be included on receipt/quote.
                ITEM QUANTITY:
                    The number to be entered into the inventory database of the product.
                ITEM COST:
                    The original purchase cost of the item being entered.
                ITEM PRICE:
                    An optional input to change to a set price for resale. This will be later utilized by the POS system.
                ITEM MARKUP:
                    An optional input to increase the ITEM PRICE by a percentage value instead, using this will increase the price by the percentage entered, and then round up
                    to the nearest .99
                VENDOR:
                    An input to assign vendor for replenishing stock.
                CATEGORY:
                    Further organization feature, to break down items for niche applications or sale. (This would be like a store that sells electronics breaking down into
                    sub categories like "Computer Parts", "Charging Accessories", "Mobile Devices", etc., or a car repair shop breaking things down into "Alternators", 
                    "Mufflers", "Wheels", "Tires", etc.)
                BRAND:
                    This could be useful for tracking how much a certain brand of item sells in comparison to others, and help determine future purchases based on name 
                    recognition, reliability, etc.
                TAXABLE:
                    Tracking whether or not the item in inventory was purchased via tax exemption, or is something that is considered taxable in your area of operation. Could also
                    track store use items that have already had tax paid on them.

    Labor/Invoicing:
        An optional subsystem combining POS attributes, Inventory attributes, and a ticketing system, to track the status of projects for repair shops in various industries,
        and allow them to adjust labor cost as line items for invoicing, which could also be imported into the POS system when applicable.

    !!!PROJECT IS SHIFTING GEARS A BIT!!!
        Coding language is currently solely python, and after evaluating the scope of things I would like this project to do, and keep things neat, organized, and somewhat presentable,
        I've decided to restructure the backend from scratch, and present it as a python powered API to handle JSON requests from a react front end. This should enable the end user to easily spin
        this up in a docker container, and then have a webmin style access point in which to update things via browser onto a local database. This would make things easier for future extensions
        or features, like if the project decided to incorporate web stores etc. into an optional feature for small business, that way POS-i-i-M could be a one stop do it all solution for 
        people trying to start a business from scratch, without needing to commit to a subscription based service until they've outgrown what this project can offer, if they ever do.
