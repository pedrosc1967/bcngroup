**TestBCNCgroup.py**

Test para recorrer las secciones del menú “HOME” y “WHO WE ARE”, para extraer el valor de los párrafos que estén dentro 
de los divs con la clase “text”.

Para ejecutarlo se puede lanzar desde un IDE como PyCharm con la opción _"Run > Run"_
También es posible ejecutarlo desde la línea de comandos mediante el comando `phton3 TestBCNCgroup.py`

**BDD correspondiente**

Feature: Extraer el valor de los párrafos en las secciones "HOME" y "WHO WE ARE"

  Scenario: Extraer los párrafos dentro de los divs con la clase "text"
    Given: un usuario abre la página de BCNCGROUP
    When: navega a la seccion <seccion>
    Then: extrae los párrafos dentro de los divs con la clase text
    
  Examples:
    | seccion    |
    | HOME       |
    | WHO WE ARE |  
    
    

