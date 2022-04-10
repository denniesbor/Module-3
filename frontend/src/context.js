import React, { useState, useContext, useEffect } from 'react'
import axios from "axios";
const AppContext = React.createContext()


const AppProvider = ({ children }) => {

    const [text, setText] = useState('');
    const [loading, setLoading] = useState(false);
    const [restaurants, setRestaurants] = useState([])
    const [availableProducts, setAvailableProducts] = useState([])
    const [suggestions, setSuggestions] = useState([])
  
    // side renders
    useEffect(() => {
      const loadFood = async() => {
        try {
          const response = await axios.get("http://127.0.0.1:8000/api/food")
          setAvailableProducts(response.data.available_food)
        } catch (error) {
          console.log(error)
        }
        
      }
  
      loadFood()
     
    }, [text]);
  
    // post request
  
    const handleSubmit = async (e) => {
      e.preventDefault();
      setRestaurants([])
      setSuggestions([])
      const postObj = {
        content: text
      }
      setText('')
  
//   if(availableProducts.includes(text)){
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
//   }
  
    //   else {
    //     // setText('a');
    //   }
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
      setSuggestions(matches)
      setText(text)
    }
  
    // search handler
  
    const searchSubmit =(suggestion) => {
      setText(suggestion)
      setSuggestions([suggestion])
      
    }

  return (
    <AppContext.Provider value={{text,
        loading,
        restaurants,
        availableProducts,
        suggestions,
        setText,
        setLoading,
        setRestaurants,
        setAvailableProducts,
        setSuggestions,
        handleSubmit,
        removeRestaurant,
        onChangeHandler,
        searchSubmit
    }}>
      {children}
    </AppContext.Provider>
  )
}
// make sure use
export const useGlobalContext = () => {
  return useContext(AppContext)
}

export { AppContext, AppProvider }