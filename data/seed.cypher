// Create Power Stations
CREATE (p1:PowerStation {name:"SolarPlant1", type:"solar", capacity:100})
CREATE (p2:PowerStation {name:"WindFarm1", type:"wind", capacity:150})
CREATE (p3:PowerStation {name:"HydroPlant1", type:"hydro", capacity:200})

// Create Substations
CREATE (s1:Substation {name:"SubstationA"})
CREATE (s2:Substation {name:"SubstationB"})
CREATE (s3:Substation {name:"SubstationC"})

// Create Consumers
CREATE (c1:Consumer {name:"Factory1", type:"industrial"})
CREATE (c2:Consumer {name:"Home1", type:"private"})
CREATE (c3:Consumer {name:"Factory2", type:"industrial"})
CREATE (c4:Consumer {name:"Mall1", type:"commercial"})

// Power stations supply substations
CREATE (p1)-[:SUPPLIES]->(s1)
CREATE (p2)-[:SUPPLIES]->(s2)
CREATE (p3)-[:SUPPLIES]->(s3)

// Substations distribute electricity
CREATE (s1)-[:DISTRIBUTES]->(c1)
CREATE (s2)-[:DISTRIBUTES]->(c2)
CREATE (s3)-[:DISTRIBUTES]->(c3)
CREATE (s3)-[:DISTRIBUTES]->(c4)