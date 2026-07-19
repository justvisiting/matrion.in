# matrion.in

Marketing site for **Matrion** — AI consulting, products and Forward Deployed Engineers.

Static single-page site, no build step. `index.html` is the whole site.

## Hosting

GitHub Pages, served at [matrion.in](https://matrion.in) via the `CNAME` file in this repo.

### DNS (GoDaddy)

| Type | Name | Value |
|---|---|---|
| A | `@` | `185.199.108.153` |
| A | `@` | `185.199.109.153` |
| A | `@` | `185.199.110.153` |
| A | `@` | `185.199.111.153` |
| CNAME | `www` | `justvisiting.github.io` |

The `www` CNAME points at the GitHub **account** host, not this repo — the `CNAME`
file above is what routes the domain to this repo.

## Local preview

```bash
python3 -m http.server 8000
# then open http://localhost:8000
```
