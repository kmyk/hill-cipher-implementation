# Hill cipher encrypter/decrpyter

## usage

encryption:

``` sh
$ python3 a.py --alphabet ABCDEFGHIJKLMNOPQRSTUVWXYZ --key GYBNQKURP encrypt CAT
FIN
```

decryption:

``` sh
$ python3 a.py --alphabet ABCDEFGHIJKLMNOPQRSTUVWXYZ --key GYBNQKURP decrypt FIN
CAT
```

The example above is one of examples in the (current) wikipedia, see <https://en.wikipedia.org/wiki/Hill_cipher>.


Also this tool supports long keys:

``` sh
$ python3 a.py --alphabet 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ123456789_{}' --key '32Cu3pmhGoyf}mY1}8Os4Hrd}Ife5k2qJRT2mQJLu8QkU5m_ANB8S3x5GF5VFcDP' decrypt '7Nv7}dI9hD9qGmP}CR_5wJDdkj4CKxd45rko1cj51DpHPnNDb__EXDotSRCP8ZCQ'
IceCTF{linear_algebra_plus_led_zeppelin_are_a_beautiful_m1xture}
```

## thanks

The function `modinv` comes from <https://github.com/sasinha/HillCipher/blob/master/Cipher.py>.
