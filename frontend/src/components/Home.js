import React,{useState} from 'react';
import axios from "axios";
import Cookies from 'js-cookie';
import {data} from './test';

import Loading from './Loading';
import Restaurants from './Restaurants';

function Home() {
  const [text, setText] = useState('');
  const [loading, setLoading] = useState(false);
  const [restaurants, setRestaurants] = useState([])

  // post request
  let csrfToken = Cookies.get('csrftoken');

  const handleSubmit = async (e) => {
    e.preventDefault();
    setLoading(true)
    setRestaurants([])
    const postObj = {
      content: text
    }

    axios.defaults.xsrfHeaderName = "X-CSRFTOKEN";
    axios.defaults.xsrfCookieName = "csrftoken";
    axios.defaults.headers = {
      "Content-Type": "application/json",
    };
    
    await axios.post("http://127.0.0.1:8000/api/sentiment", postObj)
      .then(res => {
        if (res.status === 201) {
          console.log(res.data);
        }
      })
    setRestaurants(data)
    setLoading(false)
    setText('')
  }

  //  the response is restaurants and reviews are

  const removeRestaurant = (id) => {
    const newRestaurants = restaurants.filter((restaurant) => restaurant.id !== id)
    setRestaurants(newRestaurants)
  }


  return (
    <section className="section-center">
        <form className='search-form' onSubmit={e => handleSubmit(e)}>

        <h3>Search Form</h3>
        <div className='form-control'>
          <input
            type='text'
            className='grocery'
            placeholder='e.g. Jollof Rice'
            value={text}
            onChange={(e) => setText(e.target.value)}
          />
          <button type='submit' className='submit-btn'>
            submit
          </button>
        </div>
      </form>
      {loading && <Loading />}
      {restaurants && <Restaurants restaurants={restaurants} removeRestaurant={removeRestaurant}/>}
    </section>
  )
}

export default Home