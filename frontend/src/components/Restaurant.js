import React, { useState } from 'react';
import Reviews from './Reviews';
import { Link } from 'react-router-dom';

const Restaurant = ({ business_id, restaurant_name, stars_avg, sentiment_score, reviews, removeRestaurant }) => {
  const [readReviews, setReadReviews] = useState(false);
  return (
    <article className="single-tour">
      <footer>
        <Link to={`/business/${business_id}`} className="single-restaurant">
          <h4>{restaurant_name}</h4>
        </Link>
        <div className="tour-info">
          <h4 className="tour-price">Score {sentiment_score}</h4>
          <h4 className="tour-price">Rating {stars_avg}</h4>
        </div>

        {readReviews && < Reviews reviews = {reviews}/>}
        <button onClick={() => setReadReviews(!readReviews)}>
            <p>
        {readReviews ? 'Hide Reviews' : 'Read Reviews'}
            </p>
        </button>
    
        <button className="delete-btn" onClick={() => removeRestaurant(business_id)}>
          Not Interested
        </button>
      </footer>
    </article>
  );
};

export default Restaurant;