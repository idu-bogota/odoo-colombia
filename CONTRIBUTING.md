### Contributing to Odoo-Colombia

*Vinculo rapido a la [planilla bug](https://raw.githubusercontent.com/odoo-colombia/odoo-colombia/master/ISSUE_TEMPLATE.md).*

Bienvenido! Si, vale la pena de unirse a los desarolladores de la localizacion colombiana. Estmos todos bienvenidos, expertos, idealistas, enthusiasticos, novices...

```
Vemos la posibilidad de crear un ecosistema con una fuerte dinamica en donde clientes, partners, utilizadores y otros trabajan juntos para solucionar cada vez problemas mas especificas y para **crecer como communidad entera** abriendo nuevos mercados. Seamos ambiciosos y sacamos SIGO del mercado! - Pues, adelante!
```
#### Como desarollar
Para el repositorio official mantenemos un ["Feature Branch Workflow"](https://www.atlassian.com/es/git/workflows#!workflow-feature-branch)
Los desarolladores "de confianca" (basado en el merito dentro de la communidad) son los que obtienen acceso push al repositorio official y son los que organizan la integracion del trabajo de los demas.

Para poder contribuir ya, utiliza por favor el ["Workflow Bifurcado"](https://www.atlassian.com/es/git/workflows#!workflow-forking) junto con ["Pull Requests"](https://www.atlassian.com/es/git/workflows#!pull-request)

Addicionalmente, aprender todo sobre ...
- [... git.](https://www.atlassian.com/es/git/)
- [... estilo de codigo pep8.](http://recursospython.com/pep8es.pdf) - Travis-CI con flake lo discubre! ;)
- [... Travis-CI.](http://docs.travis-ci.com/user/getting-started/)
- [... Odoo Runbot.](http://runbot.odoo.com/runbot) - hacer click en una rueda dentada y seleccionar una de las opciones `connect`

Travis-CI va verificar si el servidor puede ser contruido (inluyendo pruebas pep8) en cada commit y en cada pull request.

#### Raportar Issues
- Por favor - si se puede - raportar problemas ya con la solucion en una forma de "pull request". Estamos todos voluntarios :)

- Si despues de crear un "issue" puedes contribuir con una solucion, no olvides de referenciar el "issue" en el pull.

- Si no encuentras una solucion y despues un tiempo rasonable de buscar (estamos todos voluntarios!), por favor no hesita a redactar un "Issue" para que quede registrado y no se olvidara utilizando esta ***[planilla](https://raw.githubusercontent.com/odoo-colombia/odoo-colombia/master/ISSUE_TEMPLATE.md)***.

- Por favor no utilizar este repositorio para problemas que no son especificas de la localizacion. No queremos perder el enfoque!

#### Para que version se hace el parche?
- Por el momento queremos crear una localisacion "8.0-ready". Por ende, trabajamos simepre sobre la ultima version saas de Odoo que se supone version "stable" en que la probabibilad de un error de ser del lado de odoo core es muy bajo.
- [Obtener esta version en 20 min.](https://github.com/odoo-colombia/odoo-vagrant)


#### Proceso de Revision del codigo
- Assegurar que no hay errores en los servidores de integracion continuada.
- Discussion sobre un pull request y applicacion de "labels" indicativos.
- Felicitaciones, cuando este todo listo, incorporamos tu codigo en la localizacion official!
