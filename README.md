# Webhook
## Search users of misalud by id assigned by us

The webhook expose two directions:
* *_by_id_*: Return the user dictionary search by id
  * _id_ : String that represents id of user
  > /by_id/?id=@contact.referrer_id
* _*by_phone*_: Search user by phone number
  * _phone_ : Phone number of contact
  > /by_phone/?phone=@contact.phone
