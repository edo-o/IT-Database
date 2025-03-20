from app import db, Solution, app
with app.app_context():
    db.create_all()

s1 = Solution(problem="No sound on laptop", solution="Check if sound muted")
s2 = Solution(problem="Wifi not working", solution="Restart router, check network settings")
db.session.add(s1)
db.session.add(s2)
db.session.commit()

Solution.query.all()