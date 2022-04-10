import Loading from './Loading';
import NoMatch from './NoMatch'
import Restaurants from './Restaurants';

import { useGlobalContext } from '../context';

function Home() {

  const {text,
    loading,
    restaurants,
    suggestions,
    handleSubmit,
    removeRestaurant,
    onChangeHandler,
    searchSubmit
  } = useGlobalContext()

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

  <h3>Hello! Enter your menu or food choice in the box below and we'll match you to the best restaurants.</h3>
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