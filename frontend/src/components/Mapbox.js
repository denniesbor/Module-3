import React, { useEffect, useState } from 'react';
import mapboxgl from '!mapbox-gl'; // eslint-disable-line import/no-webpack-loader-syntax
import Map, {Marker} from 'react-map-gl';
import axios from 'axios';
import { Link, useParams } from 'react-router-dom';

import Reviews from './Reviews';
import Loading from './Loading';
import { useGlobalContext } from '../context';

const TOKEN = 'pk.eyJ1IjoibmRhcnVwZXRybyIsImEiOiJjbDFvbmN2djMwNXp3M2NrYjRzM3NsOHJjIn0.3n8aCZ3AcjQZ0ESVA9gTaQ';

mapboxgl.accessToken = TOKEN;

export default function Mapbox(props) {
  const {loading, setLoading} = useGlobalContext();
  const [readReviews, setReadReviews] = useState(false);
  const [zoom, setZoom] = useState(9);
  const [post, setPost] = useState({})
  
  const business_id = useParams().id;


  useEffect(() => {

    setLoading(true)
    const loadFood = async() => {
      try {
        const response = await axios.get(`http://127.0.0.1:8000/api/restaurant/${business_id}/`)
        // console.log(response.data)
        setPost(response.data.content)
        setLoading(false)
      } catch (error) {
        console.log(error)
        setLoading(false)
      }
      
    }

    loadFood()
  }, [business_id,setLoading]);

  // const restaurant = restaurants.find(res => res.business_id === business_id)
  // console.log(post)

  console.log(!(Object.keys(post).length === 0))
  if(loading){

    return <Loading />
  }

  if(!(Object.keys(post).length === 0)) {
    
    return (
    <section className="section-center">
        <div className="map-sidebar">
          <h3>{post.restaurant_name} | {post.location.city} City</h3>
        </div>
      <div className="map-container">
        <Map
          initialViewState={{
            longitude: post.location.longitude,
            latitude:  post.location.latitude,
            zoom: zoom,
            width: "100%",
            height: "100%",
            center:[post.location.longitude,post.location.latitude]
          }}
          mapStyle='mapbox://styles/mapbox/streets-v11'
          mapboxAccessToken={TOKEN}
          >
          <Marker longitude={post.location.longitude} latitude={post.location.latitude}>
              <img
                style={{ height: 50, width: 50 }}
                src="https://xuonginthanhpho.com/wp-content/uploads/2020/03/map-marker-icon.png"
              />
          </Marker> 
        </Map>;
    </div>
    <div className="map-footer">
        {readReviews && < Reviews reviews = {post.reviews}/>}
        <button className="btn" onClick={() => setReadReviews(!readReviews)}>
            <p>
        {readReviews ? 'Hide Reviews' : 'Read Reviews'}
            </p>
        </button>
    </div>

    </section>

  )
  }
}