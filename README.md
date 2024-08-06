**For java project**
How to deploy java application to kubernetes cluster
**step-1**

spring.application.name=demo
server.port=8092

spring.datasource.driver-class-name=com.mysql.cj.jdbc.Driver
spring.datasource.url=jdbc:mysql://mysql-service:3306/nimai_phase2?autoreconnect=true"
#spring.datasource.url=jdbc:mysql://localhost:3306/nimai?autoreconnect=true"
spring.datasource.username=admin
#spring.datasource.password=root
spring.datasource.password=admin

spring.jpa.show-sql=true

jwt.secret=fUpsaakqwzCeSnoVpFX/smX+mOnzLDSH4x0jfuw1eHkw4K7Lp7WcWsM0vOXbk/njjp3+n2cgwqUnWKXppVhptg==
jwt.expiration=3600
logging.level.org.springframework.security=DEBUG
logging.level.com.example.demo=DEBUG

# Set the root logging level
logging.level.root=INFO

# Set the logging level for your application package
logging.level.com.springboot.web=DEBUG

# Configure the log file path
logging.file.name=D:/logs/spring-boot-application.log

# Configure the logging pattern for the file
logging.pattern.file=%d{yyyy-MM-dd HH:mm:ss} [%thread] %-5level %logger{36} - %msg%n

# Configure the logging pattern for the console
logging.pattern.console=%d{yyyy-MM-dd HH:mm:ss} [%thread] %-5level %logger{36} - %msg%n

```shell
#!/bin/bash

# This is a sample shell script
echo "Hello, World!"

```bash

