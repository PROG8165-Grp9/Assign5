curl -X POST -d "username=ganda&password=Yara112809" http://127.0.0.1:8000/auth/token/

eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ1c2VyX2lkIjoxLCJlbWFpbCI6ImdhbmRhYnVyYUBob3RtYWlsLmNvbSIsInVzZXJuYW1lIjoiZ2FuZGEiLCJleHAiOjE0OTI5MzEwOTZ9.XS5EvVvtQrj-KWi92sfuocFL941e64p06uX-fs7Bbgo

curl -H "Authorization: JWT eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ1c2VyX2lkIjoxLCJlbWFpbCI6ImdhbmRhYnVyYUBob3RtYWlsLmNvbSIsInVzZXJuYW1lIjoiZ2FuZGEiLCJleHAiOjE0OTI5MzE0MjB9.y_U3ZsTRgkBUpcm1DR7sU_tsyjHLg1XuMuGShCHQeoM" http://127.0.0.1:8000/users/

curl http://127.0.0.1:8000/users/
