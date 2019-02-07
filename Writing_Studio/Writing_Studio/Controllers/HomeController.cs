using System;
using System.Collections.Generic;
using System.Linq;
using System.Web;
using System.Web.Mvc;
using System.IO;

namespace Writing_Studio.Controllers
{
    public class HomeController : Controller
    {
        public ActionResult Index()
        {
            ViewData["Message"] = "Writing Center";

            return View();
        }

        public ActionResult About()
        {
            ViewBag.Message = "Your application description page.";

            return View();
        }

        public ActionResult Contact()
        {
            ViewBag.Message = "Your contact page.";

            return View();
        }
        public ActionResult Tips()
        {
            return View();
        }
        public ActionResult Faq()
        {
            return View();
        }
       
        
        public ActionResult Schedules()
        {
            return View();
        }
        public ActionResult Appointments()
        {
            return View();
        }
        [HttpPost]
        public ActionResult Appointments(HttpPostedFileBase file)
        {


            if (file != null)
            {
                string FileName = Path.GetFileName(file.FileName);
                string path = Server.MapPath("~/Content/Essay.docx");
                file.SaveAs(path);
            }
            ViewBag.FileStatus = "File uploaded successfully.";



            return View("Appointments");
        }
    }
}