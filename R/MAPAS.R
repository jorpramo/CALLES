# install.packages("ggmap")
# install.packages("RODBC")
# install.packages("rworldmap")
# install.packages("igraph")
library(ggmap)
library("RODBC")

library(rworldmap)
library(RODBC)
library(stringr)
library(igraph)


myconn <-odbcConnect("CARRERS", uid="loginR", pwd="loginR")

municipios <- sqlQuery(myconn, "SELECT CPRO,CMUN, NOMBRE FROM [CARRERS].[dbo].[MUNICIPIOS] where nombre in ('Valencia','Madrid','Barcelona','Sevilla','Bilbao')")
municipios$CMUN<-str_pad(municipios$CMUN,3,pad = "0")
municipios$CPRO<-str_pad(municipios$CPRO,2,pad = "0")

par(mfrow=c(2,2))

spain.limits <- geocode(c("Vivero, Spain","Tenerife, Spain","Menorca, Spain"))

total_fuera<-data.frame(tipo=character(), nombre=character(),latitud=numeric(),longitud=numeric())

#hacia fuera, calles en la capital con nombre de población
for (i in 1:nrow(municipios)) {
  nombre=municipios[i,]$NOMBRE
  datos <- sqlQuery(myconn, paste("SELECT '",nombre,"',[TVIA],[NVIA]  , Latitud, longitud   FROM [CARRERS].[dbo].[VIAS] v join dbo.MUNICIPIOS on NVIA=NOMBRE
                   where v.cmum='",municipios[i,]$CMUN,"' and v.CPRO='",municipios[i,]$CPRO,"'", sep=""))
  total_fuera<-rbind(total_fuera, datos)
}  
summary(total_fuera[,1])

total_dentro<-data.frame(tipo=character(), nombre=character(),latitud=numeric(),longitud=numeric(), comunidad=character())
#hacia dentro
for (i in 1:nrow(municipios)) {
  nombre=municipios[i,]$NOMBRE
  datos <- sqlQuery(myconn, paste("SELECT '",nombre,"',[TVIA],m.nombre  , Latitud, longitud  , com.NOMBRE
FROM [CARRERS].[dbo].[VIAS] v join dbo.MUNICIPIOS m on v.cpro =m.CPRO and m.CMUN=v.cmum 
                                  join dbo.COMUNIDAD_PROVINCIA com on com.CPRO=m.cpro
                                  where nvia='",nombre,"'", sep=""))
  total_dentro<-rbind(total_dentro, datos)
}  
summary(total_dentro[,1])

for (i in 1:nrow(municipios)) {
datos <- sqlQuery(myconn, paste("SELECT [TVIA],[NVIA]  , Latitud, longitud   FROM [CARRERS].[dbo].[VIAS] v join dbo.MUNICIPIOS on NVIA=NOMBRE
                   where v.cmum='",municipios[i,]$CMUN,"' and v.CPRO='",municipios[i,]$CPRO,"'", sep=""))
newmap <- getMap(resolution = "low")
plot(newmap,
     xlim = range(spain.limits$lon),
     ylim = range(spain.limits$lat),
     asp = 1
)
points(gsub(",", ".", datos$longitud), gsub(",", ".", datos$Latitud), col = "red", cex = .6)
}

dev.new()
municipios <- sqlQuery(myconn, "SELECT distinct NOMBRE, latitud, longitud, habitantes  FROM [CARRERS].[dbo].[MUNICIPIOS] where CPRO=46")

enlaces <- sqlQuery(myconn, "SELECT distinct  orig.NOMBRE as [from], dest.NOMBRE as [to] FROM [CARRERS].[dbo].[VIAS] v join 
                    dbo.MUNICIPIOS dest on NVIA=NOMBRE join dbo.MUNICIPIOS orig on v.CMUM=orig.CMUN  where v.CPRO=46 and dest.CPRO=46 and orig.CPRO=46")

g <- graph_from_data_frame(enlaces, directed=TRUE, vertices=municipios)

V(g)$name
plot(g)
# dibujar con pesos
#plot(g, edge.width=E(g)$weight, vertex.size=V(g)$weight*10)

length(E(g))
graph.density(g)

#cercania a otros nodos
head(sort(closeness(g), decreasing=F),5)

# importancia, nodos que llegan a el
sort(betweenness(g), decreasing=F)[1:5]

#numero de enlances
sort(degree(g,mode="in"), decreasing=T)[1:10]
sort(degree(g,mode="out"), decreasing=T)[1:10]
g<-upgrade_graph(g)
valencia<-graph.neighborhood(g, 1, "Valencia",mode="in")
Gandia<-graph.neighborhood(g, 1, "Gandia",mode="in")
Alzira<-graph.neighborhood(g, 1, "Alzira",mode="in")

g1<-valencia%u%Gandia%u%Alzira
c1<-cluster_edge_betweenness(g1)
plot(c1, g1)

#comunidades 
comunidades<-edge.betweenness.community(g)
max(comunidades$membership)
plot(comunidades, g, vertex.size=4, vertex.label.cex=0.5)

# close(myconn)
