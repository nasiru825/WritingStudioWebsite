using Microsoft.Owin;
using Owin;

[assembly: OwinStartupAttribute(typeof(Writing_Studio.Startup))]
namespace Writing_Studio
{
    public partial class Startup
    {
        public void Configuration(IAppBuilder app)
        {
            ConfigureAuth(app);
        }
    }
}
