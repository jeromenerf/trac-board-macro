from genshi.core import Markup
from trac.wiki.macros import WikiMacroBase
from trac.wiki import Formatter
import StringIO

class BoardMacro(WikiMacroBase):
    """
    Returns a 4 columns board for the provided milestone
    """
    def expand_macro(self, formatter, name, text, args):
        """
        Returns some wiki text, interpreted
        """
        wikitext="""{{{
#!div style='float:left; width:23%%'

= TODO =

[[TicketQuery(status=new|reopened,milestone=%(milestone)s,format=count)]]

[[TicketQuery(status=new|reopened,order=priority,milestone=%(milestone)s,format=table,col=summary,priority)]]

}}}


{{{
#!div style='float:left; width:23%%' 

= DOING =
[[TicketQuery(status=accepted|assigned,milestone=%(milestone)s,keywords!~=test,format=count)]]

[[TicketQuery(status=accepted|assigned,order=priority,milestone=%(milestone)s,keywords!~=test,format=table,col=summary|owner)]]

}}}


{{{
#!div style='float:left; width:23%%' 

= TEST =
[[TicketQuery(status=accepted|assigned,keywords~=test,milestone=%(milestone)s,format=count)]]

[[TicketQuery(status=accepted|assigned,order=priority,keywords~=test,milestone=%(milestone)s,format=table,col=summary|owner)]]

}}}


{{{
#!div style='float:left; width:23%%' 

= DONE =
[[TicketQuery(status=closed,milestone=%(milestone)s,format=count)]]

[[TicketQuery(status=closed,order=changetime,desc=1,milestone=%(milestone)s,format=table,col=resolution|summary)]]

}}}

{{{
#!div style='clear:both'
}}}""" % {'milestone': text}

        out = StringIO.StringIO()
        Formatter(self.env, formatter.context).format(wikitext, out)
        Markup(out.getvalue()) 
        return Markup(out.getvalue())
