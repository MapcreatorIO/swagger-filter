# swagger-filter
Allows filtering of swagger.yml for multi target documentation. This repo is currently 
still a stub. The proposed command line arguments and their usage is ducumented in here.

```bash
# removes all extensions (x-*)
swagger-filter -i petstore.yml -o petstore-clean.yml --remove-extensions
# filters out x-debug: true and x-internal: true
swagger-filter -i petstore.yml -o petstore-production.yml --exclude debug --exclude internal
# stdin & stdout by default
cat petstore.yml | swagger-filter --remove-extensions > petstore-clean.yml
```
