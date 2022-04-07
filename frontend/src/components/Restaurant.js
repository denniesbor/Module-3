import React, { useState } from 'react';
import Reviews from './Reviews';

const Restaurant = ({ business_id, stars_avg, sentiment_score, reviews, removeRestaurant }) => {
  const [readReviews, setReadReviews] = useState(false);
  return (
    <article className="single-tour">
      <footer>
        <div className="tour-info">
          <h4>{business_id}</h4>
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