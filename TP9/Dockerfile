FROM openjdk:11-jre-slim
WORKDIR /app
COPY ClientUDP.java ..
RUN javac ClientUDP.java
CMD ["java", "ClientUDP"]

