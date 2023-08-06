import { ae as ordered_colors } from './index.9d2aeb7b.js';

const get_next_color = (index) => {
  return ordered_colors[index % ordered_colors.length];
};

export { get_next_color as g };
