namespace Writing_Studio.Migrations
{
    using System;
    using System.Data.Entity.Migrations;
    
    public partial class AddAge : DbMigration
    {
        public override void Up()
        {
            AddColumn("dbo.AspNetUsers", "Age", c => c.String());
        }
        
        public override void Down()
        {
            DropColumn("dbo.AspNetUsers", "Age");
        }
    }
}
