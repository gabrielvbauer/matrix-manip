from mathh.entities.point_2d import Point2D

def calc_center(point: Point2D, width: float, height: float) -> tuple[float, float]:
  x_center = point.x + width / 2;
  y_center = point.y + height / 2;
  
  return (float(x_center), float(y_center));