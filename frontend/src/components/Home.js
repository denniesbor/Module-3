import React,{useState,useEffect} from 'react';
import axios from "axios";
import Loading from './Loading';
import NoMatch from './NoMatch'
import Restaurants from './Restaurants';

function Home() {
  const [text, setText] = useState('');
  const [loading, setLoading] = useState(false);
  const [restaurants, setRestaurants] = useState([])
  const [availableProducts, setAvailableProducts] = useState([])
  const [suggestions, setSuggestions] = useState([])
  const [match, setMatch] = useState(false)


  // side renders
  useEffect(() => {
    const loadFood = async() => {
      try {
        const response = await axios.get("http://52.90.233.21/api/food")
        console.log(response.data)
        setAvailableProducts(response.data.available_food)
      } catch (error) {
        console.log(error)
      }
      
    }

    loadFood()
   
  }, []);

  // post request

  const handleSubmit = async (e) => {
    e.preventDefault();
    setRestaurants([])
    setSuggestions([])
    const postObj = {
      content: text
    }
    setText('')

    if(availableProducts.includes(text)){
      setLoading(true)
      axios.defaults.xsrfHeaderName = "X-CSRFTOKEN";
      axios.defaults.xsrfCookieName = "csrftoken";
      axios.defaults.headers = {
        "Content-Type": "application/json",
      };
      
      await axios.post("http://127.0.0.1:8000/api/sentiment", postObj)
        .then(res => {
          if (res.status === 201) {
            setRestaurants(res.data.content);
          }
        })
    }

    else {
      // setText('a');
    }
    setLoading(false)
  }

  //  the response is restaurants and reviews are

  const removeRestaurant = (business_id) => {
    const newRestaurants = restaurants.filter((restaurant) => restaurant.business_id !== business_id)
    setRestaurants(newRestaurants)
  }

  // render suggestions to the user
  const onChangeHandler = (text) =>{
    setRestaurants([])
    let matches = []
    if(text.length > 0){
      matches = availableProducts.filter(product => {
        const regex = new RegExp(text, "gi");
        return product.match(regex)
      })
    } 
    console.log(matches)
    setSuggestions(matches)
    setText(text)
  }

  // search handler

  const searchSubmit =(suggestion) => {
    setText(suggestion)
    setSuggestions([suggestion])
    
  }
    console.log(text.length)
    return (
      <section className="section-center">
          < Form handleSubmit = {handleSubmit} text ={text} onChangeHandler={onChangeHandler}/>
        {suggestions.length < 1 && text.length > 0 ? <NoMatch /> : suggestions.slice(0,10).map((suggestion,i) => {
         return <div key={i} className="suggestion">
            <button type='submit' className='search-button' onClick={() => searchSubmit(suggestion)}>
            <p>{suggestion}</p>
            </button></div>
        }) }
        {loading && <Loading />}
        {restaurants && <Restaurants restaurants={restaurants} removeRestaurant={removeRestaurant}/>}
      </section>
    )
}

const Form = ({handleSubmit,text,onChangeHandler}) => {
  return <form className='search-form' onSubmit={e => handleSubmit(e)}>

  <h3>Search Form</h3>
  <div className='form-control'>
    <input
      type='text'
      className='grocery'
      placeholder='e.g. Jollof Rice'
      value={text}
      onChange={(e) => onChangeHandler(e.target.value)}
    />
    <button type='submit' className='submit-btn'>
      submit
    </button>
  </div>
</form>

}

export default Home