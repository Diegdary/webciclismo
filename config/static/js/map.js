    const arraycordenadas = [
        [
            {lng: -74.78636308514314, lat: 10.986759946187245},
            {lng: -74.79339760335087, lat: 10.96518417905596}
        ],
        [
            {lng: -74.8005964026915, lat: 10.994465065133092},
            {lng: -74.7999223674192, lat: 10.981893185489945}
        ],
        [
            {lng: -74.80043793307173, lat:11.026559978952022},
            {lng: -74.77316920339825, lat: 10.998894679475555}
        ],
        [
            {lng: -74.80882505054734, lat: 10.996202971357675},
            {lng: -74.8038725923254, lat: 11.001841067431613}
        ],
        [
            {lng: -74.79193356617466, lat: 10.990840721435617},
            {lng: -74.8233077361051, lat: 11.002976076805751}
        ],
        [
            {lng: -74.77530225938347, lat: 10.948371468555735},
            {lng: -74.78039980038542, lat: 10.936330380877592}
        ],
        [
            {lng: -74.83412921514203, lat: 11.007852631625624},
            {lng: -74.8377794250375, lat: 11.00495947164255}
        ],
        
    ]
    let firstchanged = false;
    mapboxgl.accessToken = 'pk.eyJ1Ijoiam9qbWEiLCJhIjoiY2xubmtjbnIyMDU0YjJqcXRpbm1oMGxzbiJ9.ig6XODhbgh-3yzG7aeytzQ';
    var map = new mapboxgl.Map({
    container: 'map',
    style: 'mapbox://styles/mapbox/streets-v11',
    center: [-74.78819050532397, 10.988379510867086],
    zoom: 16
    
    });
    mirarRoute1();
    map.addControl(new mapboxgl.NavigationControl(), 'bottom-right');
    map.addControl(new mapboxgl.FullscreenControl(), 'bottom-right'); 
    map.addControl(new MapboxGeocoder({accessToken: mapboxgl.accessToken,mapboxgl: mapboxgl})); 
    map.addControl(
    new mapboxgl.GeolocateControl({
    positionOptions: {
    enableHighAccuracy: true
    },
    trackUserLocation: true,
    showUserHeading: true
    }), 'bottom-right'
    );
    
    
    
    let startMarker = null;
    let endMarker = null;
    
    function addMarker(lng, lat) {
    let markerImage = new Image(70, 42); 
    markerImage.src = 'https://freepngimg.com/thumb/bicycle/6-2-bicycle-png-7.png'; 
    if (!startMarker) {
    startMarker = new mapboxgl.Marker({ element: markerImage, anchor: 'bottom' }).setLngLat([lng, lat]).addTo(map);
    } else if (!endMarker) {
    endMarker = new mapboxgl.Marker({ element: markerImage, anchor: 'bottom' }).setLngLat([lng, lat]).addTo(map);
    calculateRoute();
    
    }
    }
    
    function calculateRoute() {
    const startCoordinates = startMarker.getLngLat();
    const endCoordinates = endMarker.getLngLat();
    
    fetch(`https://api.mapbox.com/directions/v5/mapbox/cycling/${startCoordinates.lng},${startCoordinates.lat};${endCoordinates.lng},${endCoordinates.lat}?access_token=${mapboxgl.accessToken}&geometries=geojson`)
    .then(response => response.json())
    .then(data => {
        if(!firstchanged){
            arraycordenadas.map((item,index)=>{
                if (map.getLayer(`route${index}`)) {
                    map.removeLayer(`route${index}`);
                }
                if (map.getSource(`route${index}`)) {
                    map.removeSource(`route${index}`);
                }
                
            })
            firstchanged=true;
        }
    
    
    if (map.getLayer('route')) {
        map.removeLayer('route');
    }
    if (map.getSource('route')) {
        map.removeSource('route');
    }
    
    map.addLayer({
        "id": "route",
        "type": "line",
        "source": {
        "type": "geojson",
        "data": {
            "type": "Feature",
            "geometry": data.routes[0].geometry
        }
        },
        "layout": {
        "line-join": "round",
        "line-cap": "round"
        },
        "paint": {
        "line-color": "#017ACC",
        "line-width": 4
        }
    });
    console.log(data.routes[0].geometry);
    });
    }
    
    map.on('click', (e) => {
    const lngLat = e.lngLat;
    addMarker(lngLat.lng,  lngLat.lat);
    });
    
    
    map.on('click', (e) => {
    if (endMarker && endMarker.getElement().contains(e.originalEvent.target)||startMarker && startMarker.getElement().contains(e.originalEvent.target)) {
    endMarker.remove();
    startMarker.remove();
    endMarker = null;
    startMarker = null;
    map.removeLayer('route');
    map.removeLayer('route');
    mirarRoute1();
    firstchanged=false
    }
    });
    
    function mirarRoute1() {
    
    
        //iterador
    arraycordenadas.map((item, index)=>{
        fetch(`https://api.mapbox.com/directions/v5/mapbox/cycling/${item[0].lng},${item[0].lat};${item[1].lng},${item[1].lat}?access_token=${mapboxgl.accessToken}&geometries=geojson`)
        .then(response => response.json())
        .then(data => {
        if (map.getLayer('route')) {
            map.removeLayer('route');
        }
        if (map.getSource('route')) {
            map.removeSource('route');
        }
    
        map.addLayer({
            "id": `route${index}`,
            "type": "line",
            "source": {
            "type": "geojson",
            "data": {
                "type": "Feature",
                "geometry": data.routes[0].geometry
            }
            },
            "layout": {
            "line-join": "round",
            "line-cap": "round"
            },
            "paint": {
            "line-color": "#017ACC",
            "line-width": 4
            }
        });
        console.log(index + ":")
        console.log(data.routes[0].geometry);
        });
    
    })
    
}


