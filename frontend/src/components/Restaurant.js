import React, { useState } from 'react';
import Review from './Review';

const Restaurant = ({ id, image, info, name, price, removeRestaurant }) => {
  const [readReviews, setReadReviews] = useState(false);
  return (
    <article className="single-tour">
      <footer>
        <div className="tour-info">
          <h4>{name}</h4>
          <h4 className="tour-price">${price}</h4>
        </div>
        <p>
          {readReviews && < Review info = {info}/>}
          <button onClick={() => setReadReviews(!readReviews)}>
            {readReviews ? 'Hide Reviews' : 'Read Reviews'}
          </button>
        </p>
        <button className="delete-btn" onClick={() => removeRestaurant(id)}>
          Not Interested
        </button>
      </footer>
    </article>
  );
};

export default Restaurant;